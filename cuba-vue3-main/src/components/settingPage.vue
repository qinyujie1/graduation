<template>
    <div class="card-header-right">
        <ul class="list-unstyled card-option" :style="{width:isOpen ? '230px': ''}">
          <li>
            <div><i class="fa fa-spin fa-cog" :class="{'icon-angle-double-right': isOpen}" @click.prevent="disp"></i></div>
          </li>
          <li><i class="view-html fa fa-code" @click="code()"></i></li>
          <li><i class="icofont icofont-maximize full-card" :class="display?'icofont-resize':''" @click="maximize()"></i></li>
          <li><i class="icofont icofont-minus minimize-card" :class="display?'icofont-plus':''"  @click="minimize()"></i></li>
          <li><i class="icofont icofont-refresh reload-card" @click="reload()"></i></li>
          <li><i class="icofont icofont-error close-card" @click.prevent="del()"></i></li>
        </ul>
      </div>
</template>
<script>
export default{
    name:'settingPage',
    props:{
        // id:String
    },
    data(){
            return{
            isOpen:false,
            display:false,
            full:false,
            active: false,
            load:true,
        }},
        methods:
        {
          code(){
            this.active=!this.active
            this.$emit('show',this.active)
          },
          maximize(){
            this.full= !this.full
            this.$emit('max',this.full)
          },
          minimize(){
            this.display =!this.display
            this.$emit('min',this.display)
          },
          del(){
            this.$emit('delete')
          },
            disp()
            {
                this.isOpen= !this.isOpen
            },
            reload(){
              this.load=!this.load
              this.$emit('loading',this.load)
            }
        }
}
</script>