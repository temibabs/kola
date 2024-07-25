<!-- frontend/src/views/Products.vue -->

<template>
  <div>
    <h1>Products</h1>
    <div class="masonry-layout">
      <div v-for="product in products" :key="product.id" class="product-item">
        <img :src="product.image_url" @click="viewProduct(product.id)" />
        <p>{{ product.name }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      products: []
    }
  },
  mounted() {
    this.fetchProducts()
  },
  methods: {
    fetchProducts() {
      axios.get('http://localhost:8000/products').then(response => {
        this.products = response.data
      })
    },
    viewProduct(id) {
      this.$router.push({ name: 'product-detail', params: { id: id } })
    }
  }
}
</script>

<style>
.masonry-layout {
  display: flex;
  flex-wrap: wrap;
}
.product-item {
  flex: 1 0 48%;
  margin: 1%;
}
.product-item img {
  width: 100%;
  cursor: pointer;
}
</style>
