 import products from '../../data/product.json';
 const cartItems = [];
//  (function() {
// 	var localCartItems =  JSON.parse(localStorage.getItem('cartItem')) || [];
// 	localCartItems.forEach(item=>{
// 		if(item.length!=0){
// 			cartItems.push(item)
// 		}
// 	})
// 	console.log('cartItems:',cartItems)
//    }
// )();

const state = {
	products: products.data,
	// productslist: products.data,
	cart: JSON.parse(localStorage.getItem('cartItem')) || cartItems,
	order: [],
	tagItems: [],
	filteredProduct: [],
	searchTerm: '',
    col2: false,  
    col3: false,
    col4: true,
    col6: false,
    listViewEnable: false,
    list: false,
	price: []
};
const getters = {
	price:(state)=>{
		return state.products.map((product) => {
			if(product.price){
				return product.price
			}
		})
		
	},
    col2:(state)=>{
        return state.col2 
      },
    col3:(state)=>{
        return state.col3
    },
    col4:(state)=>{
        return state.col4
    },
    col6:(state)=>{
        return state.col6
    },
    listViewEnable:(state)=>{
        return state.listViewEnable
    },
     
	getTotalAmount: (state) => {
		return state.cart.reduce((prev, curr) => {
			return prev + curr.price * curr.quantity;
		}, 0);
	},
	getBrands: (state) => {
		const brands = [...new Set(state.products.map(product => product.brand))];
		return brands;
	},
	getCategory: (state) => {
		var uniqueCategory = [];
		var itemCat = Array();
		state.products.map((product) => {
			if (product.category) {
				product.category.map((category) => {
					const index = uniqueCategory.indexOf(category);
					if (index === -1) uniqueCategory.push(category);
				});
			}
		});
		for (var i = 0; i < uniqueCategory.length; i++) {
			itemCat.push({ category: uniqueCategory[i] });
		}
		return itemCat;
	},
	getColors: (state) => {
		var uniqueColors = [];
		var itemColor = Array();
		state.products.map((product) => {
			if (product.colors) {
				product.colors.map((color) => {
					const index = uniqueColors.indexOf(color);
					if (index === -1) uniqueColors.push(color);
				});
			}
		});
		for (var i = 0; i < uniqueColors.length; i++) {
			itemColor.push({ color: uniqueColors[i] });
		}
		return itemColor;
	},
	
	filterProducts: (state) => {
		return  state.filteredProduct.filter((product) => {
		if (!state.tagItems.length) return true;
			const Tags = state.tagItems.some((prev) => { // Match Tags
				if (product.tags) {
					if (product.tags.includes(prev)) {
						return prev;
					}
				}
			});
			return Tags;
		});
	},
	getOrder: (state) => {
		return state.order;
	}
};

// mutations
const mutations = {
	// addClass:(state,payload)=>{
	// 	payload.class && document.body.setAttribute('class', payload.class)
	// },
    grid2:(state,payload)=>{
       state.col2 = payload
        state.col3 = false;
       state.col4 = false;
       state.col6 = false;
       state.listViewEnable = false;
    },
    grid3(state) {
        state.col2 = false;
        state.col3 = true;
        state.col4 = false;
        state.col6 = false;
        state.listViewEnable = false;
      },
      grid4(state) {
        state.col2 = false;
        state.col3 = false;
        state.col4 = true;
        state.col6 = false;
        state.listViewEnable = false;
      },
      grid6(state) {
        state.col2 = false;
        state.col3 = false;
        state.col4 = false;
        state.col6 = true;
        state.listViewEnable = false;
      },
      listView(state) {
        state.listViewEnable = true;
        state.list = true;
        state.col2 = false;
        state.col3 = false;
        state.col4 = false;
        state.col6 = false;
      },
      gridView(state) {
        state.listViewEnable = false;
        state.col4 = true;
      },
	addToCart: (state, payload) => {
		let hasItems = state.cart.find(items => {
			if (items.id === payload.id) {
				items.quantity = items.quantity ? items.quantity : 1;
				return true;
			}
			return false;
		});
		if (!hasItems) {
			state.cart.push(payload);
		}
		localStorage.setItem('cartItem', JSON.stringify(state.cart));
	
	},

	updateCartQuantity: (state, payload) => {
		// Calculate Product stock Counts
		function calculateStockCounts(product, quantity) {
			let qty = product.quantity + quantity;
			let stock = product.stock;
			if (stock < qty) {
				//   this.toastrService.error('You can not add more items than available. In stock '+ stock +' items.');
				return false;
			}
			return true;
		}
		state.cart.find((items, index) => {
			if (items.id === payload.product.id) {

				let qty = state.cart[index].quantity + payload.qty;
				let stock = calculateStockCounts(state.cart[index], payload.qty);
				if (qty !== 0 && stock)
					state.cart[index]['quantity'] = qty;
				
					localStorage.setItem('cartItem', JSON.stringify(state.cart));
				return true;
			}
		});
	},

	removeProduct: (state, payload) => {
		const index = state.cart.indexOf(payload);
		state.cart.splice(index,1);
		localStorage.setItem('cartItem', JSON.stringify(state.cart));
	},

	priceFilter: (state, payload) => {
		state.filteredProduct = [];
		state.products.forEach(product => {
			if (product.price >= payload.min && product.price <= payload.max) {
				state.filteredProduct.push(product);
			}
		});

	},

	setTags: (state, payload) => {
		state.tagItems = payload;
	},

	sortProducts: (state, payload) => {
		if (payload === 'a-z') {
			state.filteredProduct.sort(function (a, b) {
				if (a.name < b.name) {
					return -1;
				} else if (a.name > b.name) {
					return 1;
				}
				return 0;
			});
		} 
		// else if (payload === 'z-a') {
		// 	state.filteredProduct.sort(function (a, b) {
		// 		if (a.name > b.name) {
		// 			return -1;
		// 		} else if (a.name < b.name) {
		// 			return 1;
		// 		}
		// 		return 0;
		// 	});
		// }
          if (payload === 'low') {
			state.filteredProduct.sort(function (a, b) {
				if (a.price < b.price) {
					return -1;
				} else if (a.price > b.price) {
					return 1;
				}
				return 0;
			});
		} else if (payload === 'high') {
			state.filteredProduct.sort(function (a, b) {
				if (a.price > b.price) {
					return -1;
				} else if (a.price < b.price) {
					return 1;
				}
				return 0;
			});
		}
	},

	createOrder: (state, payload) => {
		state.order = payload;
	}
};

// actions
const actions = {
   
	addToCart: (context, payload) => {
		context.commit('addToCart', payload);
	},
	updateCartQuantity: (context, payload) => {
		context.commit('updateCartQuantity', payload);
	},
	removeProduct: (context, payload) => {
		context.commit('removeProduct', payload);
	},
	Categoryfilter: (context, payload) => {
		context.commit('Categoryfilter', payload);
	},
	sortProducts: (context, payload) => {
		context.commit('sortProducts', payload);
	},
	createOrder: (context, payload) => {
		context.commit('createOrder', payload);
	},
	priceFilter: (context, payload) => {
		context.commit('priceFilter', payload);
	},
	setTags: (context, payload) => {
		context.commit('setTags', payload);
	},
	addClass: (context, payload)=>{
		context.commit('addClass', payload)
	}
};

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};