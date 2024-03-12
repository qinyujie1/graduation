
/* eslint-disable */ 
import Layout from '../../data/layout.json';


const state = {
	layout : Layout,
    sidebarType : localStorage.getItem('SidebarType') || 'default',
	boxlayout : true,
	footer: '',
	svg:'stroke-svg',
	sidebar:'compact-sidebar1'
};

// getters
const getters = {
	footer:(state)=>{
		return state.footer
		},
			sidebar:(state)=>{
				return state.sidebar
				
			},
};

// mutations
const mutations = {
	setFooter:(state,payload)=>{
		state.footer=payload.class
	},
	set: (state) => {
		document.body.className = state.layout.color.mix_layout;
		document.body.setAttribute('main-theme-layout', 'compact-wrapper');
		document.getElementsByTagName('html')[0].setAttribute('dir', state.layout.settings.layout_type);
		var primaryColor = localStorage.getItem('primary_color') || state.layout.color.primary_color;
		var secondaryColor = localStorage.getItem('secondary_color') || state.layout.color.secondary_color;
		var layoutVersion = localStorage.getItem('layoutVersion') || state.layout.color.layout_version;
		if (primaryColor || secondaryColor) {
			addStyle(primaryColor, secondaryColor);
			if (layoutVersion)
				document.body.className = layoutVersion;
		}
	},
	setLayoutType: (state, payload) => {
		// if (payload == 'box-layout') {
		// 	document.body.classList.add(payload);
		// }
		// else if (payload == 'ltr' || payload == 'rtl') {
		// 	document.body.className = document.body.className.replace("box-layout","");
		// }
		// document.body.setAttribute('class', payload);
		// document.body.setAttribute('main-theme-layout', payload);
		document.body.classList.remove('rtl')
		document.body.classList.remove('ltr')
		document.body.classList.remove('boxed')
		document.documentElement.removeAttribute('dir')
		payload.class && document.body.setAttribute('class', payload.class);
		console.log("payload is :>",payload.class)
		payload.class && document.documentElement.setAttribute('dir', payload.class);

		// if (payload == 'ltr') {
		// 	document.body.classList.remove('rtl');
		// } else if (payload == 'rtl') {
		// 	document.body.classList.add(payload);
		// }
		state.layout.settings.layout_type = payload;
		// document.getElementsByTagName('html')[0].setAttribute('dir', payload);
	},
	setLayout: (state, payload) => {
		document.body.className = payload;
	},
	setColorScheme: (state, payload) => {
		setColor(state, payload);
		state.primaryColor = payload.primary;
		state.secondaryColor = payload.secondary;
		state.layout.color.layout_version = 'light';
		localStorage.setItem('layoutVersion', state.layout.color.layout_version);
	},
	setColorDarkScheme: (state, payload) => {
		setColor(state, payload);
		state.layout.color.layout_version = 'dark-only';
		localStorage.setItem('layoutVersion', state.layout.color.layout_version);
	},
	// setCustomizeSidebarType: (state, payload) => {
	// 	localStorage.setItem('SidebarType', payload);
	// },
	setCustomizeSidebarType: (state, payload) => {
		// var obj= document.getElementById('pageWrapper')
		
		// console.log("payload comming =>",payload)
		// if(payload=='horizontal-wrapper'){
		// 	obj.className=''
		// 	localStorage.setItem('SidebarType', payload);
		// state.sidebar=payload
		// }
		// else if(payload=='compact-sidebar1'){
		// 	obj.className=''
		// 	localStorage.setItem('SidebarType', payload);
		// state.sidebar=payload
		// }
		// else{

			localStorage.setItem('SidebarType', payload);
			// state.sidebar=
		// }
	},
	setSvg(state,payload){
		state.svg=payload
	}
};

// actions
const actions = {
	set: (context) => {
		context.commit('set');
	},
	setLayoutType: (context, payload) => {
		context.commit('setLayoutType',payload);
	},
	setLayout: (context, payload) => {
		context.commit('setLayout',payload);
	},
	setColorScheme: (context, payload) => {
		context.commit('setColorScheme',payload);
	},
	setColorDarkScheme: (context, payload) => {
		context.commit('setColorDarkScheme',payload);
	},
	// setCustomizeSidebarType: (context, payload) => {
	// 	context.commit('setCustomizeSidebarType',payload);
	// },
	setCustomizeSidebarType: (context, payload) => {
		context.commit('setCustomizeSidebarType',payload);
	},
	setSvg(context,payload){
		context.commit('setSvg',payload)
	}
};

function addStyle(primary, secondary) {
	document.documentElement.style.setProperty('--theme-deafult', primary);
	document.documentElement.style.setProperty('--theme-secondary', secondary);
}

function setColor(state, color) {
	addStyle(color.primary, color.secondary);
	localStorage.setItem('primary_color', color.primary);
	localStorage.setItem('secondary_color', color.secondary);
	// window.location.reload();
}

export default {
	namespaced: true,
	state,
	getters,
	actions,
	mutations
};
