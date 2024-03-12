<template>
  <div class="col-sm-12 box-col-12">
       <div class="card">
         <div class="card-header">
           <h3>MASONRY GALLERY</h3>
         </div>
         <div class="card-body photoswipe-pb-responsive" itemprop="associatedMedia" itemscope>
           <div
             v-masonry
             transition-duration="3s"
             item-selector=".item"
             class="masonry-container isotopeContainer row my-gallery grid gallery"
           >
             <div
               v-masonry-tile
               class="col-md-3 col-sm-6 isotopeSelector grid-item item"
               :key="index"
               v-for="(item, index) in imagearray"
               @click="() => showImg(index)"
             >
             <img :src="item.imagepath" alt="Image description" class="img-thumbnail" />
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
         id: 1,   
         imagepath: require('@/assets/images/masonry/1.jpg')
       },
       {
         id: 2,       
         imagepath: require('@/assets/images/masonry/2.jpg')
       },
       {
         id: 3,        
         imagepath: require('@/assets/images/masonry/3.jpg')
       },
       {
         id: 4,    
         imagepath: require('@/assets/images/masonry/4.jpg')
       },
       {
         id: 5,  
         imagepath: require('@/assets/images/masonry/5.jpg')
       },
       {
         id: 6,       
         imagepath: require('@/assets/images/masonry/6.jpg')
       },
       {
         id: 7,        
         imagepath: require('@/assets/images/masonry/8.jpg')
       },
       {
         id: 8,        
         imagepath: require('@/assets/images/masonry/9.jpg')
       },
       {
         id: 9,       
         imagepath: require('@/assets/images/masonry/10.jpg')
       },
       {
         id: 10,      
         imagepath: require('@/assets/images/masonry/11.jpg')
       },
       {
         id: 11,         
         imagepath: require('@/assets/images/masonry/12.jpg')
       },
       {
         id: 12,          
         imagepath: require('@/assets/images/masonry/14.jpg')
       },
       {
         id: 13,          
         imagepath: require('@/assets/images/masonry/15.jpg')
       },
       {
         id: 14,
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
},
}
</script>