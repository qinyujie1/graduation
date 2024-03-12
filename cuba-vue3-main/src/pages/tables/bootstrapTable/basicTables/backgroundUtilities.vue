<template>
  <div class="col-sm-6">
    <div class="card">
      <div class="card-header">
        <h3>Striped Row with Inverse Table</h3><span>Use <code>.table-striped</code> to add zebra-striping to any table row within the <code></code>. This styling doesn't work in IE8 and below as :nth-child CSS selector isn't supported.</span>
      </div>
      <div class="card-block row">
        <div class="col-sm-12 col-lg-12 col-xl-12">
          <div class="table-responsive">
            <table class="table table-inverse table-striped">
              <thead>
                <tr>
                  <th scope="col">Id</th>
                  <th scope="col">Dessert</th>
                  <th scope="col">Calories</th>
                  <th scope="col">Fat</th>
                  <th scope="col">Price</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">1</th>
                  <td>KitKat</td>
                  <td>518</td>
                  <td>26</td>
                  <td>20</td>
                </tr>
                <tr>
                  <th scope="row">2</th>
                  <td>Donut</td>
                  <td>452</td>
                  <td>25</td>
                  <td>80</td>
                </tr>
                <tr>
                  <th scope="row">3</th>
                  <td>Eclair</td>
                  <td>262</td>
                  <td>16</td>
                  <td>10</td>
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
        <h3>Breckpoint Specific</h3><span>Use  <code>.table-responsive"❴-sm|-md|-lg|-xl|-xxl❵"</code> functions like a heading for a table. It helps users with screen readers to find a table and understand what it’s about and decide if they want to read it.</span>
      </div>
      <div class="card-block row">
        <div class="col-sm-12 col-lg-12 col-xl-12">
          <div class="table-responsive">
            <table class="table table-responsive-sm">
              <thead>
                <tr>
                  <th scope="col">Id</th>
                  <th scope="col">Name</th>
                  <th scope="col">Order Id	</th>
                  <th scope="col">Price</th>
                  <th scope="col">Quantity</th>
                  <th scope="col">Total</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">1</th>
                  <td>Iphone X Grey	</td>
                  <td>C12345</td>
                  <td>$12550	</td>
                  <td>1</td>
                  <td>$12550</td>
                </tr>
                <tr>
                  <th scope="row">2</th>
                  <td>Titan Watch	</td>
                  <td>A14725	</td>
                  <td>$120</td>
                  <td>2</td>
                  <td>$250</td>
                </tr>
                <tr>
                  <th scope="row">3</th>
                  <td>Apple Airpods	</td>
                  <td>B54213</td>
                  <td>$210	</td>
                  <td>1</td>
                  <td>$210</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
