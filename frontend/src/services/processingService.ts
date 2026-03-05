/**
 * Serviço responsável por fazer o manejamento dos serviços de processamento
 * tanto de computação grafica, como de IA dentro do sistema de forma que 
 * todo o processamento será feito pelo backend, e somente as imagens e seus 
 * metadados serão usados dentro do frontend 
 * 
 * @class ProcessingService
 */

class ProcessingService {
    /**
     * Envia por meio do POST, uma imagem de forma que ela pode ser usada diretamente no processamento, 
     * facilitando com que a imagem caso precise
     * seja reprocessada dentro do sistema
     * * @param {File} file - O conteúdo do arquivo (glob) para ser processado
     * @returns {Promise<boolean>} - A confirmação se a imagem está sendo processada.
     * @async
     */

    // TODO: FAzer esse serviço
    async function processImagem(file: File): boolean{
        await true
        return true;
    }


}



export default ProcessingService;