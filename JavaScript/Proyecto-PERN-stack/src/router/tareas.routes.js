import Router from "express-promise-router";
import { actualizarTareas, crearTareas, eliminarTareas, listarTarea, listarTareas } from "../controllers/tareas.controller.js"

const router = Router();

router.get("/tareas", listarTareas);

router.get("/tareas/:id", listarTarea);

router.post("/tareas", crearTareas);

router.put("/tareas/:id", actualizarTareas);

router.delete("/tareas/:id", eliminarTareas);

export default router;
