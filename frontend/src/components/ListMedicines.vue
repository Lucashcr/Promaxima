<script setup>
const { result } = defineProps({
    result: Array,
    filterSelectInfo: Array
});
</script>

<template>
    <div class="container">

        <ul v-if="result.length">
            <li v-for="item in result.slice(0, 30)" :key="item.id">
                {{ item.principio_ativo }}
            </li>
        </ul>
        <p v-else>Nenhum resultado encontrado</p>
    </div>
</template>

<style scoped>
.container {
    min-width: 900px;
}
</style>

<script>
export default {
    name: "ListMedicines"
}
</script>