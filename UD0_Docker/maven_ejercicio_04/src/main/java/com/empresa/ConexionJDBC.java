package com.empresa;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.sql.ResultSet;
import java.text.NumberFormat;
import java.util.Locale;
import java.math.BigDecimal;

/**
 * Clase de ejemplo para mostrar cómo conectarse a una base de datos MariaDB
 * utilizando JDBC desde Java. 
 *
 * Crea la tabla productos, inserta algunos registros y 
 * los muestra formateados en consola.
 *
 * @author Urtzi
 * @version 1.0
 */
public class ConexionJDBC {

    /**
     * Método principal que establece conexión con la base de datos,
     * crea la tabla productos, inserta registros y realiza una consulta.
     *
     * @param args Argumentos de línea de comandos (no se usan)
     */
    public static void main(String[] args) {
        String url = "jdbc:mariadb://localhost:3306/empresa";
        String user = "root";
        String password = "admin";

        try {
            Connection conn = DriverManager.getConnection(url, user, password);
            System.out.println("Conexión establecida con la BD empresa.");

            
            Statement stmt = conn.createStatement();
            /*
            stmt.executeUpdate("CREATE TABLE IF NOT EXISTS productos (" +
                    "id INT PRIMARY KEY, " +
                    "nombre VARCHAR(50), " +
                    "precio DECIMAL(10,2))");

            stmt.executeUpdate("INSERT INTO productos VALUES (1,'Portátil',799.99)");
            stmt.executeUpdate("INSERT INTO productos VALUES (2,'Ratón',19.90)");
            stmt.executeUpdate("INSERT INTO productos VALUES (3,'Teclado',49.95)");
            */

            ResultSet rs = stmt.executeQuery("SELECT * FROM productos");
            System.out.println("Productos en la BD:");

            NumberFormat eur = NumberFormat.getCurrencyInstance(new Locale("es","ES"));

            while (rs.next()) {
                BigDecimal precio = rs.getBigDecimal("precio");
                System.out.println(rs.getInt("id") + " - " +
                                   rs.getString("nombre") + " - " +
                                   eur.format(precio));
            }

            rs.close();
            stmt.close();
            conn.close();
            System.out.println("Conexión cerrada correctamente.");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
