class Solution {
    public long minTime(int[] skill, int[] mana) {
        int n = skill.length;
        int m = mana.length;
        
        // 전체 처리 시간 (한 물약이 모든 마법사 거치는 시간)
        long totalTime = 0;
        for (int s : skill) {
            totalTime += s;
        }
        
        // 마지막 마법사가 이전 물약들 끝낸 시간
        long lastWizardFinish = totalTime * mana[0];
        
        // 각 물약 처리
        for (int j = 1; j < m; j++) {
            long prevPotionFinish = lastWizardFinish;
            
            // 역순으로 최적 시작 시간 계산
            for (int i = n - 2; i >= 0; i--) {
                // 이전 물약에서 다음 마법사가 걸린 시간 빼기
                prevPotionFinish -= (long)skill[i + 1] * mana[j - 1];
                
                // 현재 마법사의 최적 시작 시간
                lastWizardFinish = Math.max(
                    prevPotionFinish,
                    lastWizardFinish - (long)skill[i] * mana[j]
                );
            }
            
            // 현재 물약의 전체 처리 시간 더하기
            lastWizardFinish += totalTime * mana[j];
        }
        
        return lastWizardFinish;
    }
}