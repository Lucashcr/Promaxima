<script setup>
import { ref } from 'vue';

const filterBy = ref(null);
const filterValue = ref(null);

const { data } = defineProps({
    data: Array
});

function fillBlankValues(value) {
    if (typeof value === "boolean") {
        return value ? "SIM" : "NÃO";
    } else if (!value) {
        return "NÃO INFORMADO";
    }
    return value;
}

function getFilterValues(filterBy) {
    const values = new Set(
        data.map(item => fillBlankValues(item[filterBy]))
    );
    return Array.from(values).sort();
}

const FILTER_SELECT = ref([
    {
        id: "principio_ativo",
        text: "Princípio ativo",
        isChecked: false,
        type: "text",
    },
    {
        id: "cnpj",
        text: "CNPJ",
        isChecked: false,
        type: "text",
    },
    {
        id: "laboratorio",
        text: "Laboratório",
        isChecked: false,
        type: "text",
    },
    {
        id: "ggrem",
        text: "Código GGREM",
        isChecked: false,
        type: "text",
    },
    {
        id: "ean",
        text: "Registro EAN",
        isChecked: false,
        type: "text",
    },
    {
        id: "apresentacao",
        text: "Apresentação",
        isChecked: false,
        type: "text",
    },
    {
        id: "classe_terapeutica",
        text: "Classe terapêutica",
        isChecked: false,
        type: "text",
    },
    {
        id: "tipo_produto",
        text: "Tipo de Produto",
        isChecked: false,
        type: "select",
        values: getFilterValues("tipo_produto")
    },
    {
        id: "regime_preco",
        text: "Regime de preço",
        isChecked: false,
        type: "select",
        values: getFilterValues("regime_preco")
    },
    {
        id: "restricao_hospitalar",
        text: "Restrição hospitalar",
        isChecked: false,
        type: "select",
        values: getFilterValues("restricao_hospitalar")
    },
    {
        id: "cap",
        text: "Comercialização de Antimicrobianos",
        isChecked: false,
        type: "select",
        values: getFilterValues("cap")
    },
    {
        id: "confaz_87",
        text: "CONFAZ 87",
        isChecked: false,
        type: "select",
        values: getFilterValues("confaz_87")
    },
    {
        id: "icms_0",
        text: "ICMS 0%",
        isChecked: false,
        type: "select",
        values: getFilterValues("icms_0")
    },
    {
        id: "lista_ctributario",
        text: "Lista de concessão de crédito tributário (PIS/CONFINS)",
        isChecked: false,
        type: "select",
        values: getFilterValues("lista_ctributario")
    },
    {
        id: "comercializacao",
        text: "Comercialização 2022",
        isChecked: false,
        type: "select",
        values: getFilterValues("comercializacao")
    },
    {
        id: "tarja",
        text: "Tarja",
        isChecked: false,
        type: "select",
        values: getFilterValues("tarja")
    },
]);
</script>

<template>
    <div class="filterForm">
        <h2>Filtrar por: </h2>
        <div class="filterSet" v-for="item in FILTER_SELECT">
            <input type="checkbox" :name="item.id.concat('_cbx')" @change="item.isChecked = !item.isChecked">
            <label :for="item.id.concat('_cbx')">{{ item.text }}</label>
            <select v-if="item.type == 'select'" :disabled="!item.isChecked">
                <option v-for="val in item.values">{{ val }}</option>
            </select>
            <input v-else type="text" :disabled="!item.isChecked">
        </div>
    </div>
</template>

<style scoped>
.filterForm {
    display: flex;
    flex-direction: column;
    align-items: center;

    margin: 5px 0;
}

.filterForm .filterSet {
    width: 300px;
    display: grid;
}

.filterForm .filterSet input[type="checkbox"] {
    width: fit-content;
    grid-row: 1;
    grid-column: 1;
}

.filterForm .filterSet label {
    width: 275px;
    text-align: left;
    grid-row: 1;
    grid-column: 2;
}

.filterForm .filterSet select,
.filterForm .filterSet input[type="text"] {
    width: 100%;
    grid-row: 2;
    grid-column-start: 1;
    grid-column-end: 3;
}
</style>