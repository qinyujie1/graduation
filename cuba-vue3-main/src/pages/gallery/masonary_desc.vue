<template>
  <Breadcrumbs title="Masonry Gallery With Desc" main="Gallery" />
  <div class="container-fluid">
    <div class="row">
      <div class="col-sm-12">
        <div class="card">
          <div class="card-header">
            <h5>MASONRY GALLERY WITH DESCRIPTION</h5>
          </div>
          <div class="card-body">
           
                <div
                  v-masonry
                  transition-duration="3s"
                  item-selector=".item"
                  class="my-gallery row grid gallery-with-description"
                >
                  <div
                    v-masonry-tile
                    class="grid-item col-xl-3 col-sm-6 isotopeSelector item"
                    :key="index"
                    v-for="(item, index) in imagearray"
                    @click="() => showImg(index)"
                  >
                  <img :src="item.imagepath" alt="Image description" class="img-thumbnail" />

                    <div class="caption">
                      <h4>Portfolio Title</h4>
                      <p>Here is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy.</p>
                    </div>
                  </div>
                </div>
                <vue-easy-lightbox
                :visible="visible"
                :index="index"
                :imgs="lightBoxImages" 
                @hide="handleHide"
                  >
                </vue-easy-lightbox>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>
<script>
export default {
     data() {
      return {
        lightBoxImages:[],
            visible: false,
            index:'',
        imagearray: [
          {
            imagepath: require('@/assets/images/masonry/1.jpg')
          },
          {
            imagepath: require('@/assets/images/masonry/2.jpg')
          },
          {
            imagepath: require('@/assets/images/masonry/3.jpg')
          },
          {
            imagepath: require('@/assets/images/masonry/4.jpg')
          },
          {
            imagepath: require('@/assets/images/masonry/5.jpg')
          },
          {
            imagepath: require('@/assets/images/masonry/6.jpg')
          },
          {
            imagepath: require('@/assets/images/masonry/7.jpg')
          },
          {
            imagepath: require('@/assets/images/masonry/8.jpg')
          },
          {
            imagepath: require('@/assets/images/masonry/9.jpg')
          },
          {
            imagepath: require('@/assets/images/masonry/10.jpg')
          },
          {
            imagepath: require('@/assets/images/masonry/11.jpg')
          },
          {
            imagepath: require('@/assets/images/masonry/12.jpg')
          },
          {
            imagepath: require('@/assets/images/masonry/14.jpg')
          },  
          {
            imagepath: require('@/assets/images/masonry/15.jpg')
          },
          {
            imagepath: require('@/assets/images/masonry/13.jpg')
          }
        ]
      };
    },
    methods: {
      showImg (index) {
        this.index = index
        this.visible = true
      },
      handleHide () {
        this.visible = false
      },
    },
    mounted() {
      if (typeof this.$redrawVueMasonry === 'function') {
        this.$redrawVueMasonry();
      }
      this.imagearray.forEach(item=>{
            this.lightBoxImages.push(item.imagepath)
        })
    }
}
</script>