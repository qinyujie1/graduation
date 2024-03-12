<template>
  <div class="row">
    <div class="col-sm-12">
      <div class="card">
        <div class="my-gallery card-body row gallery-with-description" itemscope="">
          <div
            v-for="(src, index) in imgs"
            :key="index"
            class="col-xl-3 col-sm-6 m-0"
            @click="() => showImg(index)"
          >
            <img :src="require('../../assets/images/big-lightgallry/'+src.image)" alt="Image description" class="img-fluid" />
            <div class="caption">
           <h4> {{src.title}}</h4>
            <p>{{src.descr}}</p>
            </div>
          </div>
        </div>
        <vue-easy-lightbox
         :visible="visible"
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
    data(){
        return{
            lightBoxImages:[],
            lightBoxTitle:[],
            visible: false,
          imgs: [
         {
            title:'Johan Deo',
            descr:'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
            image:'01.jpg'
          },
          {
            title:'Dev John',
            descr:'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
            image:'02.jpg'
          },
          {
            title:'Johan Deo',
            descr:'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
            image:'03.jpg'
          },
          {
            title:'Comeren Diaz',
            descr:'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
            image:'04.jpg'
          },
          {
            title:'Andew Jon',
            descr:'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
            image:'05.jpg'
          },
          {
            title:'Sarah Loren',
            descr:'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
            image:'011.jpg'
          },
          {
            title:'Andew Jon',
            descr:'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
            image:'010.jpg'
          },
          {
            title:'Bucky Barnes',
            descr:'is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy.',
            image:'08.jpg'
          }
      ]
        }
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
    mounted(){
        this.imgs.forEach(item=>{
            this.lightBoxImages.push(require('@/assets/images/big-lightgallry/'+item.image))
            this.lightBoxTitle.push(item.title)
        })
        
        console.log(this.lightBoxImages)
    }
};
</script>
