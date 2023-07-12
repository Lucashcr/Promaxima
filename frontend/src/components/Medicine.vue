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
    cap: "CAP",
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

for (const key in data) {
    data[key] = fillBlankValues(data[key]);
}
</script>

<template>
    <div class="Medicine">
        <h2>{{ data.produto }}</h2>
        <h3>Dados de registro:</h3>
        <table>
            <tr>
                <th>{{ text.ggrem }}</th>
                <th>{{ text.registro }}</th>
                <th>{{ text.ean1 }}</th>
                <th>{{ text.ean2 }}</th>
                <th>{{ text.ean3 }}</th>
                <th>{{ text.cnpj }}</th>
                <th>{{ text.laboratorio }}</th>
            </tr>
            <tr>
                <td>{{ data.ggrem }}</td>
                <td>{{ data.registro }}</td>
                <td>{{ data.ean1 }}</td>
                <td>{{ data.ean2 }}</td>
                <td>{{ data.ean3 }}</td>
                <td>{{ data.cnpj }}</td>
                <td>{{ data.laboratorio }}</td>
            </tr>
        </table>
        <h3>Dados medicamentais:</h3>
        <table>
            <tr>
                <th>{{ text.principio_ativo }}</th>
                <th>{{ text.apresentacao }}</th>
                <th>{{ text.classe_terapeutica }}</th>
                <th>{{ text.tipo_produto }}</th>
                <th>{{ text.restricao_hospitalar }}</th>
                <th>{{ text.tarja }}</th>
            </tr>
            <tr>
                <td>{{ data.principio_ativo }}</td>
                <td>{{ data.apresentacao }}</td>
                <td>{{ data.classe_terapeutica }}</td>
                <td>{{ data.tipo_produto }}</td>
                <td>{{ data.restricao_hospitalar }}</td>
                <td>{{ data.tarja }}</td>
            </tr>
        </table>
        <h3>Preços:</h3>
        <table>
            <tr>
                <th></th>
                <th>Sem impostos</th>
                <th>0%</th>
                <th>12%</th>
                <th>17%</th>
                <th>17% ALC</th>
                <th>17,5%</th>
                <th>17,5% ALC</th>
                <th>18%</th>
                <th>18% ALC</th>
                <th>19%</th>
                <th>20%</th>
                <th>21%</th>
                <th>22%</th>
            </tr>
            <tr>
                <th>Preço de fábrica</th>
                <td>{{ data.pf_sem_impostos }}</td>
                <td>{{ data.pf_0 }}</td>
                <td>{{ data.pf_12 }}</td>
                <td>{{ data.pf_17 }}</td>
                <td>{{ data.pf_17_alc }}</td>
                <td>{{ data.pf_17_5 }}</td>
                <td>{{ data.pf_17_5_alc }}</td>
                <td>{{ data.pf_18 }}</td>
                <td>{{ data.pf_18_alc }}</td>
                <td>{{ data.pf_19 }}</td>
                <td>{{ data.pf_20 }}</td>
                <td>{{ data.pf_21 }}</td>
                <td>{{ data.pf_22 }}</td>
            </tr>
            <tr>
                <th>Preço máximo de venda ao governo</th>
                <td>{{ data.pmvg_sem_impostos }}</td>
                <td>{{ data.pmvg_0 }}</td>
                <td>{{ data.pmvg_12 }}</td>
                <td>{{ data.pmvg_17 }}</td>
                <td>{{ data.pmvg_17_alc }}</td>
                <td>{{ data.pmvg_17_5 }}</td>
                <td>{{ data.pmvg_17_5_alc }}</td>
                <td>{{ data.pmvg_18 }}</td>
                <td>{{ data.pmvg_18_alc }}</td>
                <td>{{ data.pmvg_19 }}</td>
                <td>{{ data.pmvg_20 }}</td>
                <td>{{ data.pmvg_21 }}</td>
                <td>{{ data.pmvg_22 }}</td>
            </tr>
        </table>
        <h3>Dados tributários:</h3>
        <table>
            <tr>
                <th>{{ text.regime_preco }}</th>
                <th>{{ text.cap }}</th>
                <th>{{ text.confaz_87 }}</th>
                <th>{{ text.icms_0 }}</th>
                <th>{{ text.analise_recursal }}</th>
                <th>{{ text.lista_ctributario }}</th>
                <th>{{ text.comercializacao }}</th>
            </tr>
            <tr>
                <td>{{ data.regime_preco }}</td>
                <td>{{ data.cap }}</td>
                <td>{{ data.confaz_87 }}</td>
                <td>{{ data.icms_0 }}</td>
                <td>{{ data.analise_recursal }}</td>
                <td>{{ data.lista_ctributario }}</td>
                <td>{{ data.comercializacao }}</td>
            </tr>
        </table>
    </div>
</template>

<style scoped>
.Medicine {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    background-color: lightsteelblue;
    color: darkslategray;

    border-radius: 20px;
    margin: 20px 0;
    padding: 0 20px;

    box-shadow: 10px 10px 5px rgba(0, 0, 0, 0.3);
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

.Medicine table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 30px;
}

.Medicine table th,
.Medicine table td {
    border: 1px solid darkslategray;
    padding: 5px;
}
</style>

<script>
export default {
    name: "Medicine"
}
</script>