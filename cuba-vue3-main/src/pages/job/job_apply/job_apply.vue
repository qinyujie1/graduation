<template>
    <Breadcrumbs title="Job Apply" main="Job Search" />
    <div class="container-fluid">
    <div class="row">
        <jobtab />
        <div class="col-xl-9 xl-60 text-start">
            <div class="card">
                <div class="job-search">
                    <div class="card-body pb-0">
                        <div class="media"><img class="img-40 img-fluid m-r-20" :src="getImgUrl(jobs.image)" alt="">
                            <div class="media-body">
                                <h6 class="f-w-600">
                                    <router-link :to="{ name: 'jobdetails', params: { id: jobs.id }}">{{ jobs.title }}</router-link>
                                    <span class="pull-right"><button class="btn btn-primary" type="button"><span><i class="fa fa-check text-white"></i></span> Save this job</button></span>
                                </h6>
                                <p>{{ jobs.company }} <span>{{ jobs.city }}, {{ jobs.country }} </span><span v-html="stars(jobs.stars)"></span></p>
                            </div>
                        </div>
                        <div class="job-description">
                            <personal />
                            <education />
                            <experience />
                            <upload />
                        </div>
                    </div>
                    <div class="card-footer">
                        <button class="btn btn-primary m-r-10" type="submit">Submit</button>
                        <router-link class="btn btn-light" :to="{ name: 'jobdetails', params: { id: jobs.id }}">Cancel</router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import {
    mapState
} from 'vuex';
import router from '@/router';
import jobtab from "../job-list/jobTab.vue"
import Personal from "./personal/personalPage.vue"
import education from "./educationPage.vue"
import experience from "./experiencePage.vue"
import upload from "./uploadPage.vue"
export default {
    components: {
        jobtab,
        Personal,
        education,
        experience,
        upload
    },
    computed: {
        ...mapState({
            jobs: state => state.jobs.jobs.find(job => {
                if (parseInt(router.currentRoute._rawValue.params.id) === job.id)
                    return job;
            })
        })
    },
    methods: {
        getImgUrl(filename) {
            var images = require.context('../../../assets/images/job-search/', false, /\.jpg$/);
            return images('./' + filename);
        },
        stars(count) {
            var stars = '';

            for (var i = 0; i < 5; i++) {
                if (count > i) {
                    stars = stars + '<i class="fa fa-star font-warning"></i>';
                } else {
                    stars = stars + '<i class="fa fa-star font-warning-o"></i>';
                }
            }

            return stars;
        }
    }
}
</script>
