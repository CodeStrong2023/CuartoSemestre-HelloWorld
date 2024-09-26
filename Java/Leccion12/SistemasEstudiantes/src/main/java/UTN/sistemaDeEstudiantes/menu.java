package UTN.sistemaDeEstudiantes;

import UTN.datos.EstudianteDAO;
import UTN.dominio.Estudiante;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class menu {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("ELIGE LAS ACCION QUE DESEAS REALIZAR ");
        int opcion;
        do {
            System.out.println("1-Listar Estudiantes");
            System.out.println("2-Buscar Estudiante");
            System.out.println("3-Agregar Estudiante");
            System.out.println("4-Modificar Estudiante");
            System.out.println("5-Eliminar estudiante");
            System.out.println("6-Salir");
            System.out.println("Elige una opcion");
            opcion = entrada.nextInt();
            var estudiantesDao = new EstudianteDAO();
            if (opcion==1){
                List<Estudiante> estudiantes = estudiantesDao.listarEstudiantes();
                estudiantes.forEach(System.out::println);
            } else if (opcion==2) {
                System.out.println("Dime el id del estudiante a borrar: ");
                Estudiante estudiante_a_buscar = new Estudiante(entrada.nextInt());
                var buscando = estudiantesDao.buscarEstudiantePorId(estudiante_a_buscar);
                if (buscando){
                    System.out.println("Se encontro el estudiante: "+ estudiante_a_buscar);
                }else {
                    System.out.println("No pudo ser encontrado");
                }
            }else if (opcion==3) {
                System.out.println("A continuacion ingresa los datos del Estudiante ");
                System.out.println("ingresa el nombre del estudiante");
                entrada.nextLine(); // consumimos el salto de linea que genera el nextInt anterior
                String nombre = entrada.nextLine();
                System.out.println("ingresa el apellido del estudiante");
                String apellido = entrada.nextLine();
                System.out.println("Ingresa el email del Estudiante");
                String email = entrada.nextLine();
                System.out.println("Ingresa el Telefono del estudiante");
                String telefono = entrada.nextLine();
                Estudiante estudiante = new Estudiante(nombre,apellido,email,telefono);
                var agregando = estudiantesDao.agregarEstudiante(estudiante);
                if (agregando){
                    System.out.println("Estudiante agregado con exito: " + estudiante);
                }else{
                    System.out.println("No se agrego el estudiante");
                }
            } else if (opcion == 4) {
                System.out.println("Ingresa el id del Estudiante a modificar");
                int id_estudiante = entrada.nextInt();
                entrada.nextLine();//consumimos el salto
                System.out.println("Ingresa el nombre");
                String nombre = entrada.nextLine();
                System.out.println("Ingresa el apellido");
                String apellido = entrada.nextLine();
                System.out.println("Ingresa el numero de telefono");
                String telefono = entrada.nextLine();
                System.out.println("Ingresa el email");
                String email = entrada.nextLine();
                Estudiante estudiante = new  Estudiante(id_estudiante,nombre,apellido,telefono,email);
                var actualizando = estudiantesDao.modificarEstudiante(estudiante);
                if (actualizando){
                    System.out.println("Estudiante actualizado con exito: "+estudiante);
                }else {
                    System.out.println("No se pudo actualizar el estudiante ");
                }
            } else if (opcion ==5 ) {
                System.out.println("Ingresa el id del Estudiante a eliminar");
                int id_estudiante = entrada.nextInt();
                Estudiante estudiante = new Estudiante(id_estudiante);
                var eliminando = estudiantesDao.eliminarEstudiante(estudiante);
                if (eliminando){
                    System.out.println("Se elimino con exito el estudiante: "+ id_estudiante);
                }else {
                    System.out.println("No se borro ningun estudiante");
                }
            }
        }while (opcion>=1 && opcion<6);
    }
}
