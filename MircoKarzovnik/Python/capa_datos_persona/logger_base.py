#esta es la base para todos los demas archivos 
import logging as log

#docs.python.org/3/howto/logging.html
#llmamos una configuracion basica
log.basicConfig(level=log.DEBUG,
                format='%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos_persona/capa_datos.log'),
                    log.StreamHandler()
                ])
if __name__ == '__main__':
    log.debug('Mensaje a nivel DEBUG')
    log.info('Mensjae a nivel de info')
    log.warning('mensjae a nivel de warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')

