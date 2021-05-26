<template>
	<div>
		<!-- <vue-particles
			color="#acacac"
			:particleOpacity="0.7"
			:particlesNumber="80"
			shapeType="circle"
			:particleSize="4"
			linesColor="#acacac"
			:linesWidth="1"
			:lineLinked="true"
			:lineOpacity="1"
			:linesDistance="150"
			:moveSpeed="0.4"
			:hoverEffect="true"
			hoverMode="grab"
			:clickEffect="true"
			clickMode="push"
		>
		</vue-particles> -->
		<section class="hero is-fullheight">
			<div class="hero-head">
				<Navbar />
			</div>

			<div class="hero-body">
				<div class="container has-text-centered">
					<p class="title">Dr. Machine</p>
					<p class="subtitle">Intelligent Medical Imaging</p>
					<NuxtLink to="#" class="button is-primary"> Get started! </NuxtLink>
				</div>
			</div>

			<div class="hero-foot">
				<div class="container">
					<nav class="tabs is-boxed is-fullwidth">
						<ul>
							<li
								v-for="tab in tabs"
								:key="tab.title"
								:class="{
									'is-active': currentTab === tab.component,
								}"
							>
								<a @click="currentTab = tab.component">
									{{ tab.title }}
								</a>
							</li>
						</ul>
					</nav>
				</div>
			</div>
		</section>
		<div class="container">
			<component :is="currentTab"></component>
		</div>
	</div>
</template>

<script>
import Contact from "@/components/home/Contact";
import Introduction from "@/components/home/Introduction";
import Services from "@/components/home/Services";
import Team from "@/components/home/Team";

import Navbar from "@/components/layout/Navbar";

export default {
	layout: "just_footer",
	components: {
		Contact,
		Introduction,
		Services,
		Team,
		Navbar,
	},
	data() {
		return {
			currentTab: Introduction,
			tabs: [
				{
					title: "Introduction",
					component: Introduction,
				},
				{
					title: "Services",
					component: Services,
				},
				{
					title: "Team",
					component: Team,
				},
				{
					title: "Contact",
					component: Contact,
				},
			],
		};
	},
};
</script>

<style lang="scss" scoped>
#particles-js {
	width: 100%;
	position: fixed;
	top: 0;
	right: 0;
	bottom: 0;
	left: 0;
	z-index: 0;
}

.hero {
	background-color: $dogeblueprimary;
}

.title {
	font-size: 4rem;
	color: white;
	padding-bottom: 1rem;
}

.subtitle {
	color: whitesmoke;
	padding-bottom: 1rem;
}

.tabs a {
	color: white;
}

.tabs a:hover {
	color: $primary;
}

.tabs.is-boxed a:hover {
	background-color: lighten($color: $dogeblueprimary, $amount: 10);
}
</style>
