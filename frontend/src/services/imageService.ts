class ImageService {
  static async sendImage(file: File): Promise<boolean> {
    console.log(`Sending the files: ${file}`)
    const formData = new FormData()
    formData.append('file', file)

    const response = await fetch('http://localhost:8000/api/v1/images', {
      method: 'POST',
      body: formData,
    })

    if (response.ok) {
      return true
    }

    return false
  }
}

export default ImageService
