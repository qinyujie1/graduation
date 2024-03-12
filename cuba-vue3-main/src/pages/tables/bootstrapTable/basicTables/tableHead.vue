<template>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Responsive Tables With Light Background</h3><span>A <code>.table-responsive , .table-light</code> inside table element.</span>
      </div>
      <div class="card-block row">
        <div class="col-sm-12 col-lg-12 col-xl-12">
          <div class="table-responsive">
            <table class="table table-light">
              <thead>
                <tr>
                  <th scope="col">Id</th>
                  <th scope="col">Task</th>
                  <th scope="col">Email</th>
                  <th scope="col">Phone</th>
                  <th scope="col">Assign</th>
                  <th scope="col">Date</th>
                  <th scope="col">Price   </th>
                  <th scope="col">Status</th>
                  <th scope="col">Progress</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">1</th>
                  <td>Web Development	</td>
                  <td>Pixel@efo.com	</td>
                  <td>+91 7874226671	</td>
                  <td>Mark Jecno	</td>
                  <td>12/07/2022	</td>
                  <td>$2315.00	</td>
                  <td class="font-danger">Pending</td>
                  <td>75%</td>
                </tr>
                <tr>
                  <th scope="row">2</th>
                  <td>Graphic Design	</td>
                  <td>Strap@google.com	</td>
                  <td>+91 8347855785	</td>
                  <td>Elana John	</td>
                  <td>23/08/2022	</td>
                  <td>$4125.00	</td>
                  <td class="font-danger">Pending	</td>
                  <td>45%</td>
                </tr>
                <tr>
                  <th scope="row">3</th>
                  <td>WordPress</td>
                  <td>Pixelstrap@gmail.com	</td>
                  <td>+91 635609347	</td>
                  <td>John Deo</td>
                  <td>15/04/2022	</td>
                  <td>$6123.00	</td>
                  <td class="font-success">Done</td>
                  <td>100%</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Sizing Tables</h3><span>Example of Extra large table, Add<code>.table-xl</code> class to the<code>.table</code> , Large table Add <code> .table-lg</code>  , Default table Add <code>.table-de</code>  , Small table Add <code>.table-sm </code>, Extra Small table Add <code>.table-xs</code>to create a table.</span>
      </div>
      <div class="card-block row">
        <div class="col-sm-12 col-lg-12 col-xl-12">
          <div class="table-responsive">
            <table class="table table-lg">
              <thead>
                <tr>
                  <th scope="col">Id</th>
                  <th scope="col">Employee Name</th>
                  <th scope="col">Date</th>
                  <th scope="col">Status</th>
                  <th scope="col">Hours</th>
                  <th scope="col">Performance</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">1</th>
                  <td>Mark Jecno	</td>
                  <td>22/08/2022	</td>
                  <td class="font-danger">On leave	</td>
                  <td>0</td>
                  <td>29/30</td>
                </tr>
                <tr>
                  <th scope="row">2</th>
                  <td>Elana Robbert	</td>
                  <td>21/08/2022	</td>
                  <td class="font-success">Present</td>
                  <td>10</td>
                  <td>30/30</td>
                </tr>
                <tr>
                  <th scope="row">3</th>
                  <td>John Deo	</td>
                  <td>18/08/2022</td>
                  <td class="font-danger">On leave	</td>
                  <td>8</td>
                  <td>28/30</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
