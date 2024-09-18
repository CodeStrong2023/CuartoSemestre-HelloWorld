package utn.estudiantes;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import utn.estudiantes.modelo.Estudiantes2024;
import utn.estudiantes.servicio.EstudianteServicio;

import java.util.List;
import java.util.Scanner;

@SpringBootApplication
public class EstudiantesApplication implements CommandLineRunner {
    @Autowired
    private EstudianteServicio estudianteServicio;
    private static final Logger logger = LoggerFactory.getLogger(EstudiantesApplication.class);

    String nl = System.lineSeparator();

    public static void main(String[] args) {
        logger.info("Iniciando la aplicacion...");
        //levantar la fabrica de Spring
        SpringApplication.run(EstudiantesApplication.class, args);
        logger.info("Aplicacion finalizada!");

    }

    @Override
    public void run(String... args) throws Exception {
        logger.info(nl + "Ejecutando el metodo run de Spring..." + nl);
        var salir = false;
        var consola = new Scanner(System.in);
        while (!salir) {
            mostrarMenu();
            salir = ejecutarOpciones(consola);
            logger.info(nl);
        }
    }

    private void mostrarMenu() {
        logger.info(nl);
        logger.info("""
                1. Listar Estudiante
                2. Buscar Estudiante
                3. Agregar Estudiante
                4. Modificar Estudiante
                5. Eliminar Estudiante
                6. Salir
                Elija una opcion: """);
    }

    private boolean ejecutarOpciones(Scanner consola) {
        var opcion = Integer.parseInt(consola.nextLine());
        var salir = false;
        switch (opcion) {
            case 1 -> {
                logger.info(nl + "Listado de estudiantes: " + nl);
                List<Estudiantes2024> estudiantes = estudianteServicio.listarEstudiantes();
                estudiantes.forEach((estudiante -> logger.info(estudiante.toString() + nl)));
            }
            case 2 -> {
                logger.info("Digite el id estudiante a buscar: ");
                var idEstudiante = Integer.parseInt(consola.nextLine());
                Estudiantes2024 estudiante =
                        estudianteServicio.buscarEstudiantePorId(idEstudiante);
                if (estudiante != null) {
                    logger.info("Estufiante encontrado: " + estudiante + nl);
                } else {
                    logger.info("Estudainte no encontrado: " + estudiante + nl);
                }
            }
            case 3 -> {
                logger.info("Agregar estudiante: " + nl);
                logger.info("Nombre: ");
                var nombre = consola.nextLine();
                logger.info("Apellido: ");
                var apellido = consola.nextLine();
                logger.info("Telefono: ");
                var telefono = consola.nextLine();
                logger.info("Email: ");
                var email = consola.nextLine();
                //Crear el objeto estudiante sin el id
                var estudiante = new Estudiantes2024();
                estudiante.setNombre(nombre);
                estudiante.setApellido(apellido);
                estudiante.setTelefono(telefono);
                estudiante.setEmail(email);
                estudianteServicio.guardarEstudiante(estudiante);
                logger.info("Estudiante agregado: " + estudiante + nl);
            }
            case 4 -> {//modificar estudiante
                logger.info("Modificar estudiante: " + nl);
                logger.info("Ingrese el id estudiante: ");
                var idEstudiante = Integer.parseInt(consola.nextLine());
                //buscamos el estudiante a modificar
                Estudiantes2024 estudiante =
                        estudianteServicio.buscarEstudiantePorId(idEstudiante);
                if (estudiante != null) {
                    logger.info("Nombre: ");
                    var nombre = consola.nextLine();
                    logger.info("Apellido: ");
                    var apellido = consola.nextLine();
                    logger.info("Telefono: ");
                    var telefono = consola.nextLine();
                    logger.info("Email: ");
                    var email = consola.nextLine();
                    estudiante.setNombre(nombre);
                    estudiante.setApellido(apellido);
                    estudiante.setTelefono(telefono);
                    estudiante.setEmail(email);
                    estudianteServicio.guardarEstudiante(estudiante);
                    logger.info("Estudiante modificado: " + estudiante + nl);
                } else {
                    logger.info("Estudiante No encontado con el id: " + idEstudiante);
                }
            }
            case 5 -> {//Eliminar estudiante
                logger.info("Eliminar estudiante: " + nl);
                logger.info("Digite el id estudiante: ");
                var idEstudiante = Integer.parseInt(consola.nextLine());
                //Buscamos el estudiante a eliminar
                var estudiante = estudianteServicio.buscarEstudiantePorId(idEstudiante);
                if (estudiante != null) {
                    estudianteServicio.eliminarEstudiante(estudiante);
                    logger.info("Estudiante eliminado: " + estudiante + nl);
                } else {
                    logger.info("Estudiante NO encontrado con id: " + estudiante + nl);
                }
            }
            case 6 -> {//salir
                logger.info("Hasta pronto! " + nl + nl);
                salir = true;
            }
        }

        return salir;
    }
}