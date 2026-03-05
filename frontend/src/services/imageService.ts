/**
 * Serviço responsável por gerenciar a comunicação com a API de imagens.
 * de forma a fazer somente o gerenciamento de arquivos, e não fazer a 
 * parte de solicitação e consumo do processamento das imagens
 * @class ImageService
 */
class ImageService {
  
  /**
   * Envia um arquivo de imagem para o servidor via POST.
   * * @param {File} file - O objeto de arquivo (Blob) a ser enviado.
   * @returns {Promise<boolean>} Retorna true se a imagem foi enviada com sucesso, false caso contrário.
   * @async
   */
  static async sendImage(file: File): Promise<boolean> {
    console.log(`Sending the files: ${file}`)
    const formData = new FormData()
    formData.append('file', file)

    try {
      const response = await fetch('http://localhost:8000/api/v1/images', {
        method: 'POST',
        body: formData,
      })
      return response.ok
    } catch (error) {
      console.error("Erro ao enviar imagem:", error)
      return false
    }
  }

  /**
   * Recupera a lista completa de imagens cadastradas.
   * * @returns {Promise<Array<File>>} Uma promessa que resolve em um array de arquivos.
   * @throws {Error} Dispara um erro caso a resposta da rede não seja bem-sucedida.
   * @async
   */
  static async getAllImages(): Promise<Array<File>> {
    console.log("Getting Files");
    const response = await fetch("http://localhost:8000/api/v1/images", { method: 'GET' });

    if (!response.ok) {
      throw new Error("Was not possible to fetch the images");
    }

    const data = await response.json();
    return data as Array<File>;
  }

  /**
   * Busca uma imagem específica através do seu identificador único.
   * * @param {number} id - O ID numérico da imagem no banco de dados.
   * @returns {Promise<File>} O objeto da imagem encontrada.
   * @throws {Error} Se o ID não for encontrado ou houver erro na requisição.
   * @example
   * const image = await ImageService.getImageById(10);
   * @async
   */
  static async getImageById(id: number): Promise<File> {
    const response = await fetch(`http://localhost:8000/api/v1/images/${id}`, { method: 'GET' });

    if (!response.ok) {
      throw new Error("Was not possible to fetch the image by the id");
    }

    const data = await response.json();
    return data;
  }
}

export default ImageService;