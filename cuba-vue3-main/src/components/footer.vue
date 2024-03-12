<template>
  <div>
    <footer class="footer" :class="this.footer=='footer-dark'?'footer-dark':''">
      <div class="container-fluid">
        <div class="row">
          <div class="col-md-12 footer-copyright text-center">
            <p class="mb-0">Copyright 2023 © Cuba theme by pixelstrap  </p>
          </div>
        </div>
      </div>
    </footer>
  </div>
</template>

<script>
  import json from '../data/menu';
  import { mapGetters } from 'vuex'
  export default {
    name: 'footerpage',
    data() {
      return {
        customizer: false,
        data:
          'data:text/json;charset=utf-8,' +
          encodeURIComponent(JSON.stringify(json)),
      };
    },
    computed:{
          ...mapGetters({
            footer: 'layout/footer'
          })
        }
  };
</script>
