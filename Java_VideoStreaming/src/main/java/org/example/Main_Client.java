package org.example;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class Main_Client {
    private static JFrame frame;
    private static JPanel panel;
    private static JTextField usernameField;
    private static JPasswordField passwordField;
    private static JButton signUpButton;
    private static JButton signInButton;
    private static JTextArea resultArea;

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            createAndShowGUI();
        });
    }

    private static void createAndShowGUI() {
        frame = new JFrame("Client GUI");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        panel = new JPanel();
        panel.setLayout(new GridLayout(4, 2));

        panel.add(new JLabel("Username:"));
        usernameField = new JTextField();
        panel.add(usernameField);

        panel.add(new JLabel("Password:"));
        passwordField = new JPasswordField();
        panel.add(passwordField);

        signUpButton = new JButton("Sign Up");
        signUpButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                signUp();
            }
        });
        panel.add(signUpButton);

        signInButton = new JButton("Sign In");
        signInButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                signIn();
            }
        });
        panel.add(signInButton);

        resultArea = new JTextArea();
        resultArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(resultArea);
        panel.add(scrollPane);

        frame.getContentPane().add(BorderLayout.CENTER, panel);
        frame.setSize(400, 200);
        frame.setVisible(true);
    }

    private static void signUp() {
        String username = usernameField.getText();
        String password = new String(passwordField.getPassword());
        String message = "SIGNUP:" + username + ":" + password;

        // Run network operations in a separate thread to avoid blocking the EDT
        new Thread(() -> {
            sendRequest(message);
        }).start();
    }

    private static void signIn() {
        String username = usernameField.getText();
        String password = new String(passwordField.getPassword());
        String message = "SIGNIN:" + username + ":" + password;

        // Run network operations in a separate thread to avoid blocking the EDT
        new Thread(() -> {
            boolean signInSuccessful = sendRequest(message);

            if (signInSuccessful) {
                new Thread(() -> Client.main(new String[]{})).start();
                SwingUtilities.invokeLater(() -> {
                    frame.dispose(); // Dispose the frame upon successful sign-in
                });
            }
        }).start();
    }


    private static boolean sendRequest(String message) {
        try (Socket socket = new Socket("localhost", 12345);
             BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             PrintWriter writer = new PrintWriter(socket.getOutputStream(), true)) {

            writer.println(message);
            String response = reader.readLine();

            SwingUtilities.invokeLater(() -> {
                resultArea.setText(response);
            });

            return "Success".equals(response);

        } catch (IOException e) {
            e.printStackTrace();
            JOptionPane.showMessageDialog(frame, "Error communicating with the server", "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }
    }
}
