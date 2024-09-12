package utn.estudiantes.modelo;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

@Entity
//biolerplate - codigo Repetitivo con lombok
@Data //genera setter y getters
@NoArgsConstructor //genera constructor vacio
@AllArgsConstructor //genera el constgructor con todos los argumentos
@ToString //genera el toString
public class Estudiantes2024 {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer idestudiantes2024;
    private String nombre;
    private String apellido;
    private String telefono;
    private String email;

}
