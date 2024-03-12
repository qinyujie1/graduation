<template>
   
    <breadCrumbs title="Footer Dark" main="Page Layout" title1="Footer Dark"/>
        <!-- Container-fluid starts-->
        <div class="container-fluid">
          <div class="row">
            <div class="col-sm-12">
              <div class="card">
                <div class="card-header pb-0">
                  <h3>Sample Card</h3><span>lorem ipsum dolor sit amet, consectetur adipisicing elit</span>
                </div>
                <div class="card-body">
                  <p>
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                    eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                    enim ad minim veniam, quis nostrud exercitation ullamco laboris
                    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                    in reprehenderit in voluptate velit esse cillum dolore eu fugiat
                    nulla pariatur. Excepteur sint occaecat cupidatat non proident,
                    sunt in culpa qui officia deserunt mollit anim id est laborum."
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
</template>
<script>
    export default{
        name: 'indexFooterdark',
        mounted() {
          this.$store.commit('layout/setFooter',{class:'footer-dark'})
         
        // var elems = document.getElementsByClassName('footer');
            
        // for (var i = 0; i < elems.length; i += 1) {
        //     elems[i].className += ' footer-dark';
        // }
      },
        unmounted(){
          this.$store.commit('layout/setFooter',{class:''})
            // var elems = document.getElementsByClassName('footer footer-dark');
            
            // for (var i = 0; i < elems.length; i += 1) {
            //     elems[i].className = 'footer';
            // }
        }
    }
</script>