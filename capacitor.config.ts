import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.alfereh.entfollowup',
  appName: 'Al Fereh ENT Follow-up',
  webDir: 'www',
  server: {
    androidScheme: 'https'
  },
  plugins: {
    LocalNotifications: {
      iconColor: '#10A2AE'
    }
  }
};

export default config;
