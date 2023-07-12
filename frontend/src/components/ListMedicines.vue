<script setup>
import Medicine from './Medicine.vue';

const { result } = defineProps({
    result: Array
});
</script>

<template>
    <div id="ListMedicine">
        <h1>Lista Filtrada</h1>
        <div v-if="result.length">
            <p>Quantidade de itens: {{ result.length }}</p>
            <Medicine v-for="item in result.slice(0, 20)" :data="item" />
        </div>
        <p v-else>Nenhum resultado encontrado</p>
    </div>
</template>

<style scoped>
#ListMedicine {
    min-width: 1200px;
}

#ListMedicine h1,
#ListMedicine p {
    text-align: left;
}
</style>

<script>
export default {
    name: "ListMedicines"
}
</script>