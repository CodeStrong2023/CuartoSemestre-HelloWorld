package utn.estudiantes.servicio;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import utn.estudiantes.modelo.Estudiante;
import utn.estudiantes.repositorio.EstudianteRepositorio;

@Service
public class EstudianteServicio implements IEstudianteServicio{
    @Autowired
    private EstudianteRepositorio estudianteRepositorio;

    @Override
    public List<Estudiante> listarEstudiantes() {
        List<Estudiante> estudiante = estudianteRepositorio.findAll();
        return estudiante;
    }

    public Estudiante buscarEstudiantePorId(Integer idEstudiante) {
        Estudiante estudiante = estudianteRepositorio.findById(idEstudiante).orElse(null);
        return estudiante;
    }

    public void guardarEstudiante(Estudiante estudiante) {
        estudianteRepositorio.save(estudiante);
    }

    public void eliminarEstudiante(Estudiante estudiante) {
        estudianteRepositorio.delete(estudiante);
    }
}
