export default {
    
    methods: {
      getImageUrl(path) {
        if(path)
        return require('@/assets/images/'+path)
        else
        return ''
       }
    },
  }