import Vue from 'vue'
import Router from 'vue-router'
import Products from './views/ProductList.vue'
import ProductDetail from './views/ProductDetail.vue'
import Invoices from './views/InvoiceList.vue'
import InvoiceDetail from './views/InvoiceDetail.vue'

Vue.use(Router)

export default new Router({
    routes: [
        { path: '/', name: 'products', component: Products },
        { path: '/products/:id', name: 'product-detail', component: ProductDetail },
        { path: '/invoices', name: 'invoices', component: Invoices },
        { path: '/invoices/:id', name: 'invoice-detail', component: InvoiceDetail }
    ]
})
