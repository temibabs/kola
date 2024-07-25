<template>
  <div>
    <h1>Invoice Details</h1>
    <p>Invoice Number: {{ invoice.invoice_number }}</p>
    <p>Invoice Date: {{ invoice.invoice_date }}</p>
    <p>Customer: {{ invoice.customer_info }}</p>
    <p>Supplier: {{ invoice.supplier_info }}</p>
    <ul>
      <li v-for="item in invoice.items" :key="item.id">
        {{ item.product.name }} - Quantity: {{ item.quantity }}
      </li>
    </ul>
    <p>Total Amount: {{ invoice.total_amount }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      invoice: {}
    }
  },
  mounted() {
    this.fetchInvoice()
  },
  methods: {
    fetchInvoice() {
      const id = this.$route.params.id
      axios.get(`http://localhost:8000/invoices/${id}`).then(response => {
        this.invoice = response.data
      })
    }
  }
}
</script>
