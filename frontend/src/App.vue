<script setup>

import Form from './components/Form.vue';
import MyTable from './components/MyTable.vue';

import { ref } from 'vue'

const data = ref([]);

fetch("http://localhost:8000/medicamentos/")
  .then(response => response.json())
  .then(result => {
    data.value = result;
  })
  .catch(error => console.log(error));
</script>

<template>
  <main v-if="data.length">
    <Form :data=data />
  </main>
  <main v-else>
    <p>Carregando dados...</p>
  </main>
</template>