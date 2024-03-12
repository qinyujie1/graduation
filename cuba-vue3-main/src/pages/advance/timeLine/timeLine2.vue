<template>
    <div class="container-fluid">
        <div class="row">
          <div class="col-sm-12">
            <div class="card">
              <div class="card-header pb-0">
                <h3>Example</h3>
              </div>
              <div class="card-body">
                <Timeline :value="events" align="alternate" class="customized-timeline">
                    <template #marker="slotProps">
                        <span class="custom-marker shadow-2" :style="{backgroundColor: slotProps.item.color}">
                            <i :class="slotProps.item.icon"></i>
                        </span>
                    </template>
                    <template #content="slotProps">
                        <Card>
                            <template #title>
                                {{slotProps.item.status}}
                            </template>
                            <template #subtitle>
                                {{slotProps.item.date}}
                            </template>
                            <template #content>
                                <img v-if="slotProps.item.image" :src="'demo/images/product/' + slotProps.item.image" :alt="slotProps.item.name" width="200" class="shadow-2" />
                                <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt
                                    quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!</p>
                                <Button label="Read more" class="p-button-text"></Button>
                            </template>
                        </Card>
                    </template>
                </Timeline>
              </div>
            </div>
          </div>
        </div>
      </div>
      
</template>
<script>
import Timeline from 'primevue/timeline';


export default {
    data() {
        return {
            events: [
                {status: 'Ordered', date: '15/10/2020 10:30', icon: 'pi pi-shopping-cart', color: '#9C27B0', image: 'game-controller.jpg'},
                {status: 'Processing', date: '15/10/2020 14:00', icon: 'pi pi-cog', color: '#673AB7'},
                {status: 'Shipped', date: '15/10/2020 16:15', icon: 'pi pi-shopping-cart', color: '#FF9800'},
                {status: 'Delivered', date: '16/10/2020 10:00', icon: 'pi pi-check', color: '#607D8B'}
            ],
            events2: [
                "2020", "2021", "2022", "2023"
            ]
        }
    },
    components:{
        Timeline
    }
}

</script>