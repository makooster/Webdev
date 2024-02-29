// product-detail.component.ts
export class ProductDetailComponent {
  
    shareOnWhatsApp() {
      const whatsappUrl = `whatsapp://send?text=${encodeURIComponent('Check out this product: ' + window.location.href)}`;
      window.location.href = whatsappUrl;
    }
  
    shareOnTelegram() {
      const telegramUrl = `https://t.me/share/url?url=${encodeURIComponent(window.location.href)}`;
      window.open(telegramUrl, '_blank');
    }
  }
  