<script setup>

import { ref } from 'vue'

import MedicinesDashboard from "./components/MedicinesDashboard.vue";

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
    <MedicinesDashboard :data=data />
  </main>
  <main v-else>
    <p>Carregando dados...</p>
  </main>
</template>

<style scoped>
main {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  min-height: 100vh;
}
</style>

<script>
export default {
  name: "App"
}
</script>