package UTN.datos;

import UTN.dominio.Estudiante;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;
import static UTN.conexion.Conexion.getConnection;

public class EstudianteDAO {
    //metodo listar
    public List<Estudiante> listarEstudiantes(){
        List<Estudiante> estudiantes = new ArrayList<>();
        //Creamos algunos objetos que son necesarios para comunicarnos con la base de datos
        //a travewz de PreparedStatement preparamos la sentencia para la base de datos
        PreparedStatement ps;
        //nos trae el resultado de la respuesta a la base de datos
        ResultSet rs;
        //Creamos un onjeto de tip Connection
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2024 ORDER BY idestudiantes2024";
        try {
            ps = con.prepareStatement(sql);
            rs = ps.executeQuery();
            while(rs.next()){
                var estudiante = new Estudiante();
                estudiante.setId_estudiante(rs.getInt("idestudiantes2024"));
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                //lo agregamos a la lista

                estudiantes.add(estudiante);
            }
        }catch (Exception e){
            System.out.println("Ocurrio un error al seleccionar datos: " + e.getMessage());
        }
        finally {
            try {
                //cerramos al conexion
                con.close();
            }catch (Exception e){
                System.out.println("Ocurrio un error al cerrar la conexion: "+ e.getMessage());
            }
        }
        return estudiantes;
    }

    //Metodo buscar por id -> fin by id
    public boolean buscarEstudiantePorId(Estudiante estudiante) {
        PreparedStatement ps;
        ResultSet rs;
        Connection con = getConnection();
        String sql = "SELECT * FROM estudiantes2024 WHERE idestudiantes2024 = ?";
        try {
            ps = con.prepareStatement(sql);
            ps.setInt(1,estudiante.getId_estudiante());
            rs = ps.executeQuery();
            if (rs.next()){
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                return true;
            }

        }catch (Exception e){
            System.out.println("Ocurrio una expecion: " + e.getMessage());
        }
        finally {
            try {
                con.close();
            }catch (Exception e){
                System.out.println("Ocurrio un eror al cerrar base de datos: "+ e.getMessage());
            }
        }
        return false;
    }

    //Metodo Agregar Estudiante
    public boolean agregarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "INSERT INTO estudiantes2024 (nombre,apellido,telefono,email) VALUES (?, ?, ?, ?)";
        try {
            ps = con.prepareStatement(sql);
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getTelefono());
            ps.setString(4, estudiante.getEmail());
            ps.execute();
            System.out.println("se agrego con exito el estudiante: " + estudiante);
            return true;

        }catch (Exception e){
            System.out.println("oCURRIO UN ERRO AL AGREGAR EL ESTUDIANTE: "+e.getMessage());
        }
        finally {
            try {
                con.close();
            }catch (Exception e){
                System.out.println("No se pudo cerrar la conexion: " + e.getMessage());
            }
        }
    return false;
    };
    //Metodo modificar estudiante
    public boolean modificarEstudiante(Estudiante estudiante){
      PreparedStatement ps;
      Connection con = getConnection();
      String sql = "UPDATE estudiantes2024 SET nombre=?, apellido=?, telefono=?, email=? WHERE idestudiantes2024=?";
      try {
          ps = con.prepareStatement(sql);
          ps.setString(1,estudiante.getNombre());
          ps.setString(2, estudiante.getApellido());
          ps.setString(3, estudiante.getTelefono());
          ps.setString(4, estudiante.getEmail());
          ps.setInt(5,estudiante.getId_estudiante());
          ps.execute();
          return true;
      } catch (Exception e) {
          System.out.println("No se pudo actualizar el estudiante: "+e.getMessage());
      }
      finally {
          try {
               con.close();
          }catch (Exception e){
              System.out.println("No se pudo cerrar la conexzcion:  "+e.getMessage());
          }
      }
      return false;

    };
    public boolean eliminarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getConnection();
        String sql = "DELETE FROM estudiantes2024 WHERE idestudiantes2024 = ?";
        try {
            ps = con.prepareStatement(sql);
            ps.setInt(1,estudiante.getId_estudiante());
            ps.execute();
            return true;
        } catch (Exception e){
            System.out.println("No se pudo borrar el Estudiante: "+ e.getMessage());
        }
        finally {
            try {
                con.close();
            }catch (Exception e){
                System.out.println("No se pudo cerrar la conexion: "+e.getMessage());

            }
        }
        return false;
    }

    public static void main(String[] args) {
        //Listar los estudiantes
        var estudiantesDao =new EstudianteDAO();
        System.out.println("Listado de estudiantes: ");
        List<Estudiante> estudiantes = estudiantesDao.listarEstudiantes();
        estudiantes.forEach(System.out::println);//Fucnio  lamda para imprimir
/*
        //Buscar por id
        var estudiante1 = new Estudiante(4);//el uno hace referencia al constructor que vamos a utilizar
        System.out.println("Estudiantes antes de la busqueda: " + estudiante1);
        var encontrado = estudiantesDao.buscarEstudiantePorId(estudiante1);
        if(encontrado){
            System.out.println("Estudiante encontrado: "+ estudiante1);
        }else{
            System.out.println("NO SE ENCONTRO EL ESTUDIANTE: "+estudiante1.getId_estudiante());
        }
        //Agregar estudiante
        Estudiante estudiante2= new Estudiante("Leandro","Eugenio","2625500165","leoeugenio16@gmail.com");
        estudiantesDao.agregarEstudiante(estudiante2);*/

        //MODIFICAR ESTUDIANTE
       /* var estudiante = new Estudiante(10,"Dario","Gonzalez","2604521321","Dgonzalez@gmail.com");
        var estudianteModificado = estudiantesDao.modificarEstudiante(estudiante);
        if (estudianteModificado)
            System.out.println("Estudiante modificado: "+estudianteModificado);
        else
            System.out.println("Etudiante no modificado: "+estudianteModificado);*/
        //Borrar estudiante
        var estudiante = new Estudiante(12);
        var estudianteBorrado = estudiantesDao.eliminarEstudiante(estudiante);
        if (estudianteBorrado){
            System.out.println("Se borro correctamente el estudiante: "+estudianteBorrado);
        }else {
            System.out.println("No se borro el Estudiante: "+ estudianteBorrado);
        }

    }
}

