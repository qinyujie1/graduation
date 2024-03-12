<template>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Hoverable Rows With Horizontal Border</h3><span>Hoverable row use a class  <code>table-hover</code> and for Horizontal border use a class <code>.table-border-horizontal</code> , Solid border Use a class<code>.border-solid .table</code>class.</span>
      </div>
      <div class="table-responsive signal-table">
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Id</th>
              <th scope="col">Status</th>
              <th scope="col">Signal Name	</th>
              <th scope="col">Security</th>
              <th scope="col">Stage</th>
              <th scope="col">Schedule</th>
              <th scope="col">Team Lead</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">1</th>
              <td class="d-flex align-items-center"><i class="bg-light-success font-success" data-feather="alert-triangle"></i><span class="font-success">No Signal</span></td>
              <td>Astrid: NE Shared managed</td>
              <td>Medium</td>
              <td>Triaged</td>
              <td>0.33	</td>
              <td>Chase Nguyen	</td>
            </tr>
            <tr>
              <th scope="row">2</th>
              <td class="d-flex align-items-center"><i class="bg-light-danger font-danger" data-feather="alert-triangle"></i><span class="font-danger">Offline</span></td>
              <td>Cosmo: prod shared ares	</td>
              <td>Huge</td>
              <td>Triaged</td>
              <td>0.39</td>
              <td>Brie Furman</td>
            </tr>
            <tr>
              <th scope="row">3</th>
              <td class="d-flex align-items-center"> <i class="bg-light-primary font-primary" data-feather="alert-circle"></i><span class="font-primary">Online</span></td>
              <td>Phoenix: prod shared lyra-lists	</td>
              <td>Minor</td>
              <td>No Triaged</td>
              <td>3.12	</td>
              <td>Jeremy Lake</td>
            </tr>
            <tr>
              <th scope="row">4</th>
              <td class="d-flex align-items-center"> <i class="bg-light-success font-success" data-feather="check-circle"></i><span class="font-success">No Signal</span></td>
              <td>Astrid: NE Shared managed</td>
              <td>Negligible</td>
              <td>Triaged</td>
              <td>13.18</td>
              <td>Angelica Howards</td>
            </tr>
            <tr>
              <th scope="row">5</th>
              <td class="d-flex align-items-center"> <i class="bg-light-danger font-danger" data-feather="check-circle"></i><span class="font-danger">Online</span></td>
              <td>Astrid: NE Shared managed</td>
              <td>Medium</td>
              <td>No Triaged</td>
              <td>5.33		</td>
              <td>Diane Okuma</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <div class="col-sm-12">
    <div class="card">
      <div class="card-header">
        <h3>Inverse Table with Primary background</h3><span>Use a class <code>.bg-info, .bg-success, .bg-warning and .bg-danger classes.</code> with light text on dark backgrounds inside table element.<br>To set the light background color use .bg-[color] class where [color] is the value of your selected color from stack color palette. So for teal color background class will be .bg-teal</span>
      </div>
      <div class="table-responsive">
        <table class="table table-striped bg-primary">
          <thead class="tbl-strip-thad-bdr">
            <tr>
              <th scope="col">Id</th>
              <th scope="col">First Name</th>
              <th scope="col">Last Name</th>
              <th scope="col">Company</th>
              <th scope="col">Credit Volume	  </th>
              <th scope="col">Username</th>
              <th scope="col">Role	  </th>
              <th scope="col">Country</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">1</th>
              <td>Ram Jacob	</td>
              <td>Wolfe</td>
              <td>Apple Inc.	</td>
              <td>$3500.00	</td>
              <td>RamJacob@twitter	</td>
              <td>Developer</td>
              <td>IND</td>
            </tr>
            <tr>
              <th scope="row">2</th>
              <td>John Deo		</td>
              <td>Gummer	</td>
              <td>Hewlett packard		</td>
              <td>$2400.00</td>
              <td>JohnDeo@twitter		</td>
              <td>Designer</td>
              <td>US</td>
            </tr>
            <tr>
              <th scope="row">3</th>
              <td>Elana John		</td>
              <td>Wolfe</td>
              <td>Microsoft		</td>
              <td>$2560.00	</td>
              <td>ElanaJohn@twitter	</td>
              <td>Designer</td>
              <td>UK</td>
            </tr>
            <tr>
              <th scope="row">4</th>
              <td>Meryl Streep	</td>
              <td>Roberts</td>
              <td>Tata Ltd.		</td>
              <td>$1870.00</td>
              <td>MerylStreep@twitter	</td>
              <td>Developer</td>
              <td>IND</td>
            </tr>
            <tr>
              <th scope="row">5</th>
              <td>Emma Stone	</td>
              <td>Stone</td>
              <td>Wipro Ltd.		</td>
              <td>$4580.00	</td>
              <td>EmmaStone@twitter	</td>
              <td>Developer</td>
              <td>IRN</td>
            </tr>
            <tr>
              <th scope="row">6</th>
              <td>Eliana Jons	</td>
              <td>Jons</td>
              <td>Info Ltd.		</td>
              <td>$4580.00	</td>
              <td>ElianaJons@twitter		</td>
              <td>Developer</td>
              <td>IRN</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
              
</template>
