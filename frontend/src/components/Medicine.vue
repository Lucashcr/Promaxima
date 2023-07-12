<script setup>
const { data } = defineProps({
    data: Object
});

delete data.id;

console.log(data);

const text = {
    principio_ativo: "Princípio ativo",
    cnpj: "CNPJ",
    laboratorio: "Laboratório",
    ggrem: "Código GGREM",
    registro: "Registro",
    ean1: "Registro EAN1",
    ean2: "Registro EAN2",
    ean3: "Registro EAN3",
    produto: "Produto",
    apresentacao: "Apresentação",
    classe_terapeutica: "Classe terapêutica",
    tipo_produto: "Tipo de Produto",
    regime_preco: "Regime de preço",
    pf_sem_impostos: "Preço de Fábrica (sem impostos)",
    pf_0: "Preço de Fábrica 0%",
    pf_12: "Preço de Fábrica 12%",
    pf_17: "Preço de Fábrica 17%",
    pf_17_alc: "Preço de Fábrica 17% ALC",
    pf_17_5: "Preço de Fábrica 17,5%",
    pf_17_5_alc: "Preço de Fábrica 17,5% ALC",
    pf_18: "Preço de Fábrica 18%",
    pf_18_alc: "Preço de Fábrica 18% ALC",
    pf_19: "Preço de Fábrica 19%",
    pf_20: "Preço de Fábrica 20%",
    pf_21: "Preço de Fábrica 21%",
    pf_22: "Preço de Fábrica 22%",
    pmvg_sem_impostos: "Preço Máximo de Venda ao Governo (sem impostos)",
    pmvg_0: "Preço Máximo de Venda ao Governo 0%",
    pmvg_12: "Preço Máximo de Venda ao Governo 12%",
    pmvg_17: "Preço Máximo de Venda ao Governo 17%",
    pmvg_17_alc: "Preço Máximo de Venda ao Governo 17% ALC",
    pmvg_17_5: "Preço Máximo de Venda ao Governo 17,5%",
    pmvg_17_5_alc: "Preço Máximo de Venda ao Governo 17,5% ALC",
    pmvg_18: "Preço Máximo de Venda ao Governo 18%",
    pmvg_18_alc: "Preço Máximo de Venda ao Governo 18% ALC",
    pmvg_19: "Preço Máximo de Venda ao Governo 19%",
    pmvg_20: "Preço Máximo de Venda ao Governo 20%",
    pmvg_21: "Preço Máximo de Venda ao Governo 21%",
    pmvg_22: "Preço Máximo de Venda ao Governo 22%",
    restricao_hospitalar: "Restrição hospitalar",
    cap: "Comercialização de Antimicrobianos",
    confaz_87: "CONFAZ 87",
    icms_0: "ICMS 0%",
    analise_recursal: "Análise Recursal",
    lista_ctributario: "Lista de concessão de crédito tributário (PIS/CONFINS)",
    comercializacao: "Comercialização 2022",
    tarja: "Tarja"
};

function fillBlankValues(value) {
    if (typeof value === "boolean") {
        return value ? "SIM" : "NÃO";
    } else if (!value) {
        return "NÃO INFORMADO";
    }
    return value;
}
</script>

<template>
    <div class="Medicine">
        <h3>Nome do produto: {{ data.produto }}</h3>
        <p v-for="key in Object.keys(data)">{{ text[key] }}:<br /> {{ fillBlankValues(data[key]) }}</p>
    </div>
</template>

<style scoped>
.Medicine {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    border: 1px solid black;
    border-radius: 5px;
    margin: 20px 0;
    padding: 20px;
}

.Medicine h3 {
    font-size: 1.2rem;
    margin-top: 5px;
    padding: 0;
}

.Medicine p {
    font-size: 1rem;
    margin-top: 5px;
    padding: 0;
}
</style>

<script>
export default {
    name: "Medicine"
}
</script>