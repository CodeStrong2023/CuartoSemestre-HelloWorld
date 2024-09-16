package UTN.conexion;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexion {
    public static Connection getConnection(){
        Connection conexion = null;
        //Variable para conectarnos a la base de datos
        var baseDeDatos = "estudiantes2024";
        var url = "jdbc:mysql://localhost:3306/" + baseDeDatos;
        var usuario = "root";
        var password= "root";

        //cargamos la clase del driver de mysql en memoria
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            conexion = DriverManager.getConnection(url, usuario, password);
        } catch (ClassNotFoundException | SQLException e){
            System.out.println("Ocurrio un error en la conexion: "+ e.getMessage());
        } //fin catch
        return conexion;
    }//fin metodo conexion
}
