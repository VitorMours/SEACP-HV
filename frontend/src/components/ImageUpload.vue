<script setup lang="ts">
import { ref, reactive } from 'vue';

const processing = ref(false);
const file = ref<File | null>(null);
const showModal =ref(false);
const result = reactive({
    filepath:"", 
    name:"", 
    mimetype:""
});

function handleFileChange(event: Event) {
    const target = event.target as HTMLInputElement
    if (target.files && target.files.length > 0) {
        file.value = target.files[0]!;
    }

}

async function toggleProcessing() {
    if (!file.value) {
        alert('Selecione um arquivo primeiro')
        return
    }

    processing.value = true

    try {
        const formData = new FormData()
        formData.append('file', file.value)
        console.log(formData);

        const response = await fetch('http://localhost:8000/api/v1/images/', {
            method: 'POST',
            body: formData,
        })
        if (!response.ok) {
            throw new Error('Erro ao processar arquivo')
        }

        const resultData = await response.json()
        console.log('Resultado:', resultData)
        Object.assign(result, {
            filepath: resultData.filepath,
            mimetype: resultData.mimetype,
            name: resultData.name
        })
        
        showModal.value = true;


    } catch (error) {
        console.error(error)
        alert('Erro no processamento')
    } finally {
        processing.value = false
    }
}

</script>

<template>

    <main class=" p-4 bg-base-300 min-h-screen">
        <section
            class="container mx-auto min-h-[89vh] shadow-sm p-4 rounded-md bg-base-100 flex justify-center content-center items-center">
            <div v-if="processing == false" class="flex flex-col gap-3 justify-center  items-center">
                <input type="file" class="file-input file-input-ghost" @change="handleFileChange">
                <button class="btn w-50" @click="toggleProcessing">
                    Iniciar Processamento
                </button>
            </div>
            <div v-else class="flex flex-col gap-3 justify-center items-center">
                <span class="loading loading-spinner loading-xl"></span>
            </div>
        </section>
    </main>
    <dialog id="success_ingestion_dialog" :open="showModal" class="modal">
        <div class="modal-box">
            <h3 class="text-xl font-bold"> Imagem processada com sucesso!</h3>
            <p class="py-4">As imagens foram processadas tendo em vista que elas possuem os seguintes metadados: </p>
            <p class="py-2"><strong>Filepath: </strong> {{ result.filepath }}</p>
            <p class="py-2"><strong>Name: </strong>{{ result.name }}</p>
            <p class="py-2"><strong>Mimetype: </strong>{{ result.mimetype }}</p>
            
            <div class="modal-action">
                <form method="dialog">
                    <!-- if there is a button in form, it will close the modal -->
                    <button class="btn">Close</button>
                </form>
            </div>
        </div>
    </dialog>
</template>