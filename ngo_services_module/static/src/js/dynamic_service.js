import publicWidget from "@web/legacy/js/public/public_widget";
import { rpc } from "@web/core/network/rpc";

publicWidget.registry.DynamicServices = publicWidget.Widget.extend({
    selector: '#explore-services',

    start() {
        console.log("DynamicServices Widget Initialized");
        this._fetchAndRenderServices();
        return this._super.apply(this, arguments);
    },

    async _fetchAndRenderServices() {
        const servicesRow = document.getElementById('dynamic-services-row');
        console.log("Services Row:", servicesRow);

        if (!servicesRow) {
            console.error("Element #dynamic-services-row not found");
            return;
        }

        servicesRow.innerHTML = '<div class="text-center">Loading services...</div>';

        try {
            const data = await rpc("/services/", { params: {} });

            console.log('Services fetched successfully:', data);

            if (data.length === 0) {
                servicesRow.innerHTML = '<div class="text-center">No services available.</div>';
                return;
            }

            servicesRow.innerHTML = data.map((service) => {
                return `
                    <div class="col-md-4">
                        <div class="card service-card my-2 shadow-sm">
                            <div class="container text-center">
                                <img class="img-fluid rounded" src="data:image/png;base64,${service.service_image}" alt="${service.service_name}" />
                                <h3 class="mt-2">${service.service_name}</h3>
                                <p>${service.banner_sub_text}</p>
                                <a href="${service.service_url}" class="btn btn-primary">Learn More</a>
                            </div>
                        </div>
                    </div>
                `;
            }).join('');
        } catch (error) {
            console.error('Error fetching services:', error);
            servicesRow.innerHTML = '<div class="text-center text-danger">Error loading services.</div>';
        }
    },
});

export default publicWidget.registry.DynamicServices;
