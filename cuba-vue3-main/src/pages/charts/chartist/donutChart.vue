<template>
<div class="col-md-6 col-sm-12 box-col-12">
    <div class="card">
        <div class="card-header pb-0">
            <h5>Animating a Donut with Svg.animate</h5>
        </div>
        <div class="card-body">

            <chartist class="ct-8 flot-chart-container" ratio="ct-major-second" type="Pie" :data="chart3.data" :options="chart3.options" :event-handlers="chart3.eventHandlers">
            </chartist>
        </div>
    </div>
</div>
</template>

<script>
import * as Chartist from 'chartist';
export default {
    data() {
        return {
            chart3: {
                data: {
                    series: [10, 20, 50, 20, 5, 50, 15],
                    labels: [1, 2, 3, 4, 5, 6, 7]
                },
                options: {
                    donut: true,
                    showLabel: false,
                },
                eventHandlers: [{
                    event: 'draw',
                    fn(data) {
                        if (data.type === 'slice') {
                            var pathLength = data.element._node.getTotalLength();
                            data.element.attr({
                                'stroke-dasharray': pathLength + 'px ' + pathLength + 'px',

                            });
                            var animationDefinition = {
                                'stroke-dashoffset': {
                                    id: 'anim' + data.index,
                                    dur: 1000,
                                    begin: 1000 * data.index,
                                    from: -pathLength + 'px',
                                    to: '0px',
                                    easing: Chartist.Svg.Easing.easeOutQuint,
                                    fill: 'freeze'
                                }
                            };
                            if (data.index !== 0) {
                                animationDefinition['stroke-dashoffset'].begin = 'anim' + (data.index - 1) + '.end';
                            }
                            data.element.attr({
                                'stroke-dashoffset': -pathLength + 'px'
                            });
                            data.element.animate(animationDefinition, false);
                        }
                    }
                }]
            },
        }
    }
}
</script>
