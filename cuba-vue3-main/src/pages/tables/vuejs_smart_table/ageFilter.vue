<template>
<div class="col-md-12">
    <div class="card">
        <div class="card-header">
            <h5 class="card-title">Age Filter</h5>
        </div>
        <div class="card-body">
            <div class="table-responsive">
                <div id="basic-1_wrapper" class="dataTables_wrapper no-footer">
                    <div class="row ">
                        <div class="col-sm-2">
                            <fieldset class="qty-box">
                                <div class="input-group bootstrap-touchspin">
                                    <button class=" btn-square bootstrap-touchspin-down" v-on:click="decrement(item)" type="button">
                                        <i class="fa fa-minus"></i></button>
                                    <input class="touchspin text-center form-control" name="item.quantity" type="text">
                                    <button class="btn btn-primary btn-square bootstrap-touchspin-up" v-on:click="increment(item)" type="button">
                                        <i class="fa fa-plus"></i></button>
                                </div>
                            </fieldset>
                        </div>
                        <div class="col-sm-2">
                            <fieldset class="qty-box">
                                <div class="input-group bootstrap-touchspin">
                                    <button class=" btn-square bootstrap-touchspin-down" v-on:click="decrement(item)" type="button">
                                        <i class="fa fa-minus"></i></button>
                                    <input class="touchspin text-center form-control" name="item.quantity" type="text">
                                    <button class="btn btn-primary btn-square bootstrap-touchspin-up" v-on:click="increment(item)" type="button">
                                        <i class="fa fa-plus"></i></button>
                                </div>
                            </fieldset>
                        </div>
                    </div>
                    <div class="dataTables_length" id="basic-1_length">
                        <table class="display dataTable" id="basic-1" :filters="agefilters">
                            <thead>
                                <tr>
                                    <th>Name</th>
                                    <th>Position</th>
                                    <th>Office</th>
                                    <th>Age</th>
                                    <th>Start date</th>
                                    <th>Salary</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="row in get_rows()" :key="row">
                                    <td>{{ row.name }}</td>
                                    <td>{{ row.position }}</td>
                                    <td>{{ row.office }}</td>
                                    <td>{{ row.age }}</td>
                                    <td>{{ row.startdate }}</td>
                                    <td>{{ row.salary }}</td>
                                </tr>
                            </tbody>
                        </table>
                        <ul class="pagination">
                            <li class="page-item">
                                <a class="page-link" href="#" aria-label="Previous">
                                    <span aria-hidden="true">&laquo;</span>
                                </a>
                            </li>
                            <li class="page-item" v-for="i in num_pages()" :key="i" v-bind:class="[i == currentPage ? 'active' : '']" v-on:click="change_page(i)"><a class="page-link">{{i}}</a></li>
                            <li class="page-item">
                                <a class="page-link" href="#" aria-label="Next">
                                    <span aria-hidden="true">&raquo;</span>
                                </a>
                            </li>
                        </ul>
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
} from "vuex";
export default {
    data() {
        return {
            elementsPerPage: 10,
            currentPage: 1,
            ascending: false,
            sortColumn: '',
            perPage: 10,
            pageOptions: [10, 25, 50, 100],
            filter: null,
        };
    },
    computed: {
        ...mapState({
            tableItems: (state) => state.table.items,
        }),
        columns() {
            if (this.tableItems.length == 0) {
                return [];
            }
            return Object.keys(this.tableItems[0])
        }
    },
    methods: {
        num_pages() {
            return Math.ceil(this.tableItems.length / this.elementsPerPage);
        },
        change_page(page) {
            this.currentPage = page;
        },
        get_rows() {
            var start = (this.currentPage - 1) * this.elementsPerPage;
            var end = start + this.elementsPerPage;
            return this.tableItems.slice(start, end);
        },

    }
};
</script>
