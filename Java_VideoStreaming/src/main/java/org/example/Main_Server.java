package org.example;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.net.ServerSocket;
import java.net.Socket;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class Main_Server {
    private final String USER_DATABASE_FILE = "userdatabase.json";
    private Map<String, User> userDatabase;
    private Gson gson = new Gson();

    private final Object initializationLock = new Object();
    private boolean isInitialized = false;

    public Main_Server() {
        new Thread(() -> Server.main(new String[]{})).start();
        synchronized (initializationLock) {
            if (!isInitialized) {
                userDatabase = readUserDatabase();
                isInitialized = true;
            }
        }
    }

    private Map<String, User> readUserDatabase() {
        try (Reader reader = new FileReader(USER_DATABASE_FILE)) {
            Type type = new TypeToken<Map<String, User>>() {}.getType();
            return gson.fromJson(reader, type);
        } catch (IOException e) {
            e.printStackTrace();
            return Collections.synchronizedMap(new HashMap<>());
        }
    }

    private void writeUserDatabase() {
        try (Writer writer = new FileWriter(USER_DATABASE_FILE)) {
            gson.toJson(userDatabase, writer);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public boolean signUp(String username, String password) {
        synchronized (initializationLock) {
            if (!isInitialized) {
                userDatabase = readUserDatabase();
                isInitialized = true;
            }
        }

        synchronized (userDatabase) {
            if (!userDatabase.containsKey(username)) {
                String hashedPassword = hashPassword(password);
                User newUser = new User(username, hashedPassword);
                userDatabase.put(username, newUser);
                writeUserDatabase();
                return true;
            }
        }
        return false;
    }

    public boolean signIn(String username, String password) {
        synchronized (initializationLock) {
            if (!isInitialized) {
                userDatabase = readUserDatabase();
                isInitialized = true;
            }
        }

        synchronized (userDatabase) {
            if (userDatabase.containsKey(username)) {
                String hashedPassword = hashPassword(password);
                User user = userDatabase.get(username);
                if (hashedPassword.equals(user.getHashedPassword())) {
                    return true;
                }
            }
        }
        return false;
    }

    private String hashPassword(String password) {
        try {
            MessageDigest md = MessageDigest.getInstance("SHA-256");
            byte[] hashedBytes = md.digest(password.getBytes());

            // Convert the byte array to a hexadecimal string
            StringBuilder hexString = new StringBuilder();
            for (byte b : hashedBytes) {
                String hex = Integer.toHexString(0xff & b);
                if (hex.length() == 1) {
                    hexString.append('0');
                }
                hexString.append(hex);
            }

            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static class User {
        private String username;
        private String hashedPassword;

        public User(String username, String hashedPassword) {
            this.username = username;
            this.hashedPassword = hashedPassword;
        }

        public String getUsername() {
            return username;
        }

        public String getHashedPassword() {
            return hashedPassword;
        }
    }

    public static void main(String[] args) {
        Main_Server server = new Main_Server();
        try {
            ServerSocket serverSocket = new ServerSocket(12345);
            System.out.println("Server is running...");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                handleClientRequest(clientSocket, server);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void handleClientRequest(Socket clientSocket, Main_Server server) {
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
             PrintWriter writer = new PrintWriter(clientSocket.getOutputStream(), true)) {

            String request = reader.readLine();
            String[] parts = request.split(":");
            if (parts.length == 3) {
                String action = parts[0];
                String username = parts[1];
                String password = parts[2];

                boolean result = false;
                if ("SIGNUP".equals(action)) {
                    result = server.signUp(username, password);
                } else if ("SIGNIN".equals(action)) {
                    result = server.signIn(username, password);
                }

                writer.println(result ? "Success" : "Failure");
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
