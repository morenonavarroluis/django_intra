 document.addEventListener('DOMContentLoaded', () => {
            const dashboardLayout = document.getElementById('dashboardLayout');
            const sidebar = document.querySelector('.sidebar');
            const menuToggle = document.getElementById('menuToggle');
            const sidebarOverlay = document.getElementById('sidebarOverlay');
            const submenuContainers = document.querySelectorAll('.has-submenu');

            // 1. Lógica para Colapsar/Expandir la Barra Lateral
            menuToggle.addEventListener('click', () => {
                // Alternar el estado en el layout principal
                dashboardLayout.classList.toggle('is-open'); 
                
                // Si el menú se abre en móvil, bloquear el scroll del cuerpo
                if (window.innerWidth < 1024 && dashboardLayout.classList.contains('is-open')) {
                    document.body.style.overflow = 'hidden';
                } else {
                    document.body.style.overflow = '';
                }
            });

            // Cerrar el sidebar al hacer clic en el overlay (solo en móvil)
            sidebarOverlay.addEventListener('click', () => {
                dashboardLayout.classList.remove('is-open');
                document.body.style.overflow = '';
            });

            // 2. Lógica para Abrir/Cerrar Submenús (Comportamiento "Accordion")
            submenuContainers.forEach(container => {
                const mainItem = container.querySelector('.main-item');
                const arrow = container.querySelector('.arrow');

                // Asegura que el estado inicial de la flecha refleje la clase 'open'
                if (container.classList.contains('open')) {
                     arrow.classList.replace('fa-chevron-down', 'fa-chevron-up');
                }

                mainItem.addEventListener('click', (e) => {
                    // Prevenir despliegue de submenú si el texto está oculto (barra lateral colapsada en desktop)
                    // La comprobación 'lg:w-16' es un indicativo del estado colapsado
                    if (window.innerWidth >= 1024 && !dashboardLayout.classList.contains('is-open') && !sidebar.matches(':hover')) {
                        // Aquí, el usuario está en desktop y el menú está en modo icono,
                        // por lo que el clic debería ignorar el despliegue del submenú.
                        return;
                    }

                    const isOpening = !container.classList.contains('open');

                    // Cierra los otros submenús (comportamiento "accordion")
                    submenuContainers.forEach(otherContainer => {
                        if (otherContainer !== container && otherContainer.classList.contains('open')) {
                            otherContainer.classList.remove('open');
                            const otherArrow = otherContainer.querySelector('.arrow');
                            if (otherArrow) {
                                otherArrow.classList.replace('fa-chevron-up', 'fa-chevron-down');
                            }
                        }
                    });

                    // Abre o cierra el submenú actual
                    container.classList.toggle('open');
                    
                    // Cambia el icono de flecha
                    if (isOpening) {
                        arrow.classList.replace('fa-chevron-down', 'fa-chevron-up');
                    } else {
                        arrow.classList.replace('fa-chevron-up', 'fa-chevron-down');
                    }
                });
            });
            
            // 3. Manejar el redimensionamiento de la ventana
            window.addEventListener('resize', () => {
                // Al volver a desktop, elimina el estilo de overflow y la clase 'is-open' si existe, para asegurar el layout
                if (window.innerWidth >= 1024) {
                    document.body.style.overflow = '';
                    dashboardLayout.classList.remove('is-open');
                }
            });
        });