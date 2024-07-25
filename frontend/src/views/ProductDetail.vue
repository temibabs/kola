<template>
  <div>
    <img :src="product.image_url" class="banner-image" />
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
    <p>Price: {{ product.price }}</p>
    <button @click="addToCart">Add To Cart</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      product: {}
    }
  },
  mounted() {
    this.fetchProduct()
  },
  methods: {
    fetchProduct() {
      const id = this.$route.params.id
      axios.get(`http://127.0.0.1:5001/api/products/${id}`).then(response => {
        this.product = response.data
      })
    },
    addToCart() {
      alert('Added to Cart')
    }
  }
}
</script>

<style>
.banner-image {
  width: 100%;
  height: 300px;
  object-fit: cover;
}
</style>
