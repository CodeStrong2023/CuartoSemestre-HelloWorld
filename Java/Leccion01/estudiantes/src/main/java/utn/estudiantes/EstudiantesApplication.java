package utn.estudiantes;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import com.sun.org.slf4j.internal.LoggerFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import utn.estudiantes.servicio.EstudianteServicio;

@SpringBootApplication
public class EstudiantesApplication implements CommandLineRunner{

	@Autowired
	private EstudianteServicio estudianteServicio;
	private static final Logger logger = LoggerFactory(EstudiantesApplication.class);

	String nl = System.lineSeparator();

	public static void main(String[] args) {
		logger.info("Iniciando la aplicación...");
		// levantar la fabrica de spring
		SpringApplication.run(EstudiantesApplication.class, args);
		logger.info("Aplicación finalizada!");
	}

	@Override
	public void run(String... args) throws Exception {
	logger.info(nl+"Ejecutando el método run de spring..."+nl);
	}
}
