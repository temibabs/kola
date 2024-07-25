<template>
  <div>
    <h1>Invoices</h1>
    <ul>
      <li v-for="invoice in invoices" :key="invoice.id" @click="viewInvoice(invoice.id)">
        Invoice #{{ invoice.invoice_number }} - {{ invoice.total_amount }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      invoices: []
    }
  },
  mounted() {
    this.fetchInvoices()
  },
  methods: {
    fetchInvoices() {
      axios.get('http://localhost:8000/invoices').then(response => {
        this.invoices = response.data
      })
    },
    viewInvoice(id) {
      this.$router.push({ name: 'invoice-detail', params: { id: id } })
    }
  }
}
</script>
