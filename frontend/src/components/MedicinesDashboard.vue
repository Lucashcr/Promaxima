<script setup>

import { ref, computed } from 'vue';

import ListMedicines from "./ListMedicines.vue";

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
    return Array.from(new Set(
        data.map(item => fillBlankValues(item[filterBy]))
    )).sort();
}

const filterSelectInfo = ref([
    {
        id: "principio_ativo",
        text: "Princípio ativo",
        isChecked: false,
        type: "text",
        currentValue: null
    },
    {
        id: "cnpj",
        text: "CNPJ",
        isChecked: false,
        type: "text",
        currentValue: null
    },
    {
        id: "laboratorio",
        text: "Laboratório",
        isChecked: false,
        type: "text",
        currentValue: null
    },
    {
        id: "ggrem",
        text: "Código GGREM",
        isChecked: false,
        type: "text",
        currentValue: null
    },
    {
        id: "ean",
        text: "Registro EAN",
        isChecked: false,
        type: "text",
        currentValue: null
    },
    {
        id: "apresentacao",
        text: "Apresentação",
        isChecked: false,
        type: "text",
        currentValue: null
    },
    {
        id: "classe_terapeutica",
        text: "Classe terapêutica",
        isChecked: false,
        type: "text",
        currentValue: null
    },
    {
        id: "tipo_produto",
        text: "Tipo de Produto",
        isChecked: false,
        type: "select",
        values: getFilterValues("tipo_produto"),
        currentValue: null
    },
    {
        id: "regime_preco",
        text: "Regime de preço",
        isChecked: false,
        type: "select",
        values: getFilterValues("regime_preco"),
        currentValue: null
    },
    {
        id: "restricao_hospitalar",
        text: "Restrição hospitalar",
        isChecked: false,
        type: "select",
        values: getFilterValues("restricao_hospitalar"),
        currentValue: null
    },
    {
        id: "cap",
        text: "Comercialização de Antimicrobianos",
        isChecked: false,
        type: "select",
        values: getFilterValues("cap"),
        currentValue: null
    },
    {
        id: "confaz_87",
        text: "CONFAZ 87",
        isChecked: false,
        type: "select",
        values: getFilterValues("confaz_87"),
        currentValue: null
    },
    {
        id: "icms_0",
        text: "ICMS 0%",
        isChecked: false,
        type: "select",
        values: getFilterValues("icms_0"),
        currentValue: null
    },
    {
        id: "lista_ctributario",
        text: "Lista de concessão de crédito tributário (PIS/CONFINS)",
        isChecked: false,
        type: "select",
        values: getFilterValues("lista_ctributario"),
        currentValue: null
    },
    {
        id: "comercializacao",
        text: "Comercialização 2022",
        isChecked: false,
        type: "select",
        values: getFilterValues("comercializacao"),
        currentValue: null
    },
    {
        id: "tarja",
        text: "Tarja",
        isChecked: false,
        type: "select",
        values: getFilterValues("tarja"),
        currentValue: null
    },
]);
const filteredData = ref(data);

const getFilteredData = () => {
    let result = Array.from(data);
    for (let item of filterSelectInfo.value) {
        if (item.isChecked) {
            result = result.filter(row => {
                if (item.type == "select") {
                    return fillBlankValues(row[item.id]) == item.currentValue;
                } else {
                    return fillBlankValues(row[item.id]).includes(item.currentValue);
                }
            });
        }
    }
    return result;
};

const filterIconColor = ref("");
function toggleFilterIcon() {
    const filterForm = document.getElementById("FilterForm");
    const filterIcon = document.querySelector("#MedicinesDashboard > button > i");
    if (filterForm.style.visibility == "visible") {
        filterForm.style.visibility = "hidden";
        filterIcon.style.color = "#E3E3E3";
    } else {
        filterForm.style.visibility = "visible";
        filterIcon.style.color = "#242424";
    }
}
</script>

<template>
    <div id="MedicinesDashboard">
        <button @click="toggleFilterIcon()">
            <i class="fa fa-filter" :color="filterIconColor"></i>
        </button>
        <div id="FilterForm">
            <h2>Filtrar por: </h2>
            <div class="FilterSet" v-for="info in filterSelectInfo" :key="info.id">
                <input type="checkbox" :name="info.id.concat('_cbx')" v-model="info.isChecked">
                <label :for="info.id.concat('_cbx')">{{ info.text }}</label>
                <select v-if="info.type == 'select'" :disabled="!info.isChecked" v-model="info.currentValue"
                    @change="console.log(info.currentValue)">
                    <option v-for="val in info.values" :key="val">{{ val }}</option>
                </select>
                <input v-else type="text" v-model="info.currentValue" :disabled="!info.isChecked">
            </div>
            <button @click="filteredData = getFilteredData()">Filtrar</button>
        </div>
        <ListMedicines :result=filteredData />
    </div>
</template>

<style scoped>
#MedicinesDashboard {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
}

i {
    position: fixed;
    z-index: 999;
    top: 0;
    left: 0;
    padding: 15px;
    font-size: 50px;
    color: antiquewhite;
}

#FilterForm {
    position: fixed;
    top: 0;
    left: 0;

    display: flex;
    flex-direction: column;
    align-items: center;

    height: 100vh;
    padding: 50px;

    background-color: lightsteelblue;
    color: darkslategrey;

    visibility: hidden;
}

#FilterForm .FilterSet {
    width: 300px;
    display: grid;
}

#FilterForm .FilterSet input[type="checkbox"] {
    width: fit-content;
    grid-row: 1;
    grid-column: 1;
}

#FilterForm .FilterSet label {
    width: 275px;
    text-align: left;
    grid-row: 1;
    grid-column: 2;
}

#FilterForm .FilterSet select,
#FilterForm .FilterSet input[type="text"] {
    grid-row: 2;
    grid-column-start: 1;
    grid-column-end: 3;
}

#FilterForm button {
    margin-top: 20px;
}
</style>

<script>
export default {
    name: "MedicinesDashboard",
}
</script>