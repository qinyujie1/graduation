<template>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Custom Table Color With Hover And Stripped</h3><span>Use class <code>table-hover, table-striped table-*table-info,table-success,table-success,table-info,table-danger,table-primary,table-secondary,table-light,table-active</code>  inside table element.</span>
      </div>
      <div class="table-responsive">
        <table class="table table-striped bg-primary hover">
          <thead class="tbl-strip-thad-bdr">
            <tr>
              <th scope="col">Id</th>
              <th scope="col">Film Title</th>
              <th scope="col">Released</th>
              <th scope="col">Studio</th>
              <th scope="col">Budget  </th>
              <th scope="col">Domestic Gross</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">1</th>
              <td>Frozen	</td>
              <td>2013	</td>
              <td>Disney	</td>
              <td>$150,000,000</td>
              <td>$400,953,009</td>
            </tr>
            <tr>
              <th scope="row">2</th>
              <td>Minions	</td>
              <td>2015	</td>
              <td>Universal	</td>
              <td>$74,000,000</td>
              <td>$336,045,770</td>
            </tr>
            <tr>
              <th scope="row">3</th>
              <td>Zootopia	</td>
              <td>2016	</td>
              <td>Disney	</td>
              <td>$150,000,000</td>
              <td>$341,268,248</td>
            </tr>
            <tr>
              <th scope="row">4</th>
              <td>Finding Dory		</td>
              <td>2016</td>
              <td>Disney	Pixar</td>
              <td>$175,000,000</td>
              <td>	$486,295,561</td>
            </tr>
            <tr>
              <th scope="row">5</th>
              <td>Toy Story 3		</td>
              <td>2010</td>
              <td>Disney	Pixar</td>
              <td>$200,000,000</td>
              <td>$415,004,880</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Dashed Border </h3><span>Dashed border use class <code>.table-dashed</code> , for Dotted border use class<code>.table-dotted</code>, for Double border use class<code>.table-Double</code></span>
      </div>
      <div class="card-block row">
        <div class="col-sm-12 col-lg-12 col-xl-12">
          <div class="table-responsive">
            <table class="table table-dashed">
              <thead>
                <tr>
                  <th scope="col">Id </th>
                  <th scope="col">Classname</th>
                  <th scope="col">Type</th>
                  <th scope="col">Hours</th>
                  <th scope="col">Trainer</th>
                  <th scope="col">Spots</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">1</th>
                  <td>Crit Cardio</td>
                  <td>Gym</td>
                  <td>9:00 AM - 11:00 AM	</td>
                  <td>Aaron Chapman	</td>
                  <td>10</td>
                </tr>
                <tr>
                  <th scope="row">2</th>
                  <td>Zumba Dance</td>
                  <td>Dance</td>
                  <td>8:00 AM - 9:00 AM		</td>
                  <td>Donna Wilson	</td>
                  <td>12</td>
                </tr>
                <tr>
                  <th scope="row">3</th>
                  <td>Like a butterfly	</td>
                  <td>Boxing</td>
                  <td>9:00 AM - 10:00 AM	</td>
                  <td>Randy Porter		</td>
                  <td>13</td>
                </tr>
                <tr>
                  <th scope="row">4</th>
                  <td>Pilates Reformer	</td>
                  <td>Gym</td>
                  <td>7:00 AM - 8:30 AM		</td>
                  <td>Aaron Chapman	</td>
                  <td>15</td>
                </tr>
                <tr>
                  <th scope="row">5</th>
                  <td>Mind & Body	</td>
                  <td>Yoga</td>
                  <td>8:00 AM - 9:00 AM		</td>
                  <td>Adam Stewart	</td>
                  <td>20</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
