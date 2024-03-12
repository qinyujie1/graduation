<template>
    <div class="col-sm-12 col-xl-6">
        <div class="card">
          <div class="card-header pb-0">
            <h3>Checkbox Tree</h3>
          </div>
          <div class="card-body">
            <div id="treecheckbox">
                <Tree :nodes="menu" :use-icon="false" :use-checkbox="true" 
                />
            </div>
          </div>
        </div>
      </div>
</template>
<script>
import Tree from "vue3-tree";
import "vue3-tree/dist/style.css"
export default {
    components: {
        Tree
    },
    data() {
        return {
          menu: [{
                    id: 1,
                    label: "Admin",
                    nodes: [{
                            id: 2,
                            label: "Assets",
                            nodes: [{
                                    id: 3,
                                    label: "CSS",
                                    nodes: [{
                                            id: 4,
                                            label: "Css One"
                                        },
                                        {
                                            id: 5,
                                            label: "Css Two"
                                        }
                                    ]
                                },
                                {
                                    id: 6,
                                    label: "Js",
                                    nodes: [{
                                            id: 7,
                                            label: "Js One"
                                        },
                                        {
                                            id: 8,
                                            label: "Js Two"
                                        }
                                    ]
                                },
                                {
                                    id: 9,
                                    label: "Scss",
                                    nodes: [{
                                            id: 10,
                                            label: "Sub Child",
                                            nodes: [{
                                                    id: 11,
                                                    label: "Sub File"
                                                },
                                                {
                                                    id: 12,
                                                    label: "Sub File"
                                                }
                                            ]
                                        },
                                        {
                                            id: 13,
                                            label: "Scss Two"
                                        }
                                    ]
                                },
                            ],
                        },
                        {
                            id: 14,
                            label: "Default",
                            nodes: [{
                                    id: 15,
                                    label: "Dashboard"
                                },
                                {
                                    id: 16,
                                    label: "Typography"
                                }
                            ]
                        }
                    ],
                },
                {
                    id: 17,
                    label: "index file"
                }
            ]
        }
    },
   
}
</script>